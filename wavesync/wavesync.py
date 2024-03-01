import numpy as np
import pywt

class WaveSync:
    def __init__(self, level_of_decomposition=4, wavelet='db4'):
        self.level_of_decomposition = level_of_decomposition
        self.wavelet = wavelet

    @staticmethod
    def normalize_vector(v):
        return v / np.linalg.norm(v)

    @staticmethod
    def create_complex_vector(v):
        half_len = len(v) // 2
        return v[:half_len] + 1j * v[half_len:]

    def compute_wavelet_transform_and_phase(self, v):
        coeffs = pywt.wavedec(v, self.wavelet, level=self.level_of_decomposition)
        phases = [np.angle(coeff) for coeff in coeffs if coeff.size > 0]
        return coeffs, phases

    @staticmethod
    def average_phase_synchrony(phases_x, phases_y):
        phase_differences = []
        for px, py in zip(phases_x, phases_y):
            phase_differences.append(px - py)
        phase_differences_flat = np.concatenate(phase_differences)
        R = np.abs(np.mean(np.exp(1j * phase_differences_flat)))
        V = 1 - R
        R_prime = R * (1 - V)
        return R_prime

    def prepare_vector(self, vec):
        normalized_vec = self.normalize_vector(vec.flatten())
        complex_vec = self.create_complex_vector(normalized_vec)
        return complex_vec

    @staticmethod
    def cosine_similarity(v1, v2):
        dot_product = np.dot(v1, v2)
        norm_product = np.linalg.norm(v1) * np.linalg.norm(v2)
        return dot_product / norm_product if norm_product else 0.0

    def compare(self, vec, vecs):
        complex_query = self.prepare_vector(vec)
        complex_vecs = [self.prepare_vector(v) for v in vecs]
        _, query_phases = self.compute_wavelet_transform_and_phase(complex_query)
        wavelet_transforms_and_phases = [self.compute_wavelet_transform_and_phase(v) for v in complex_vecs]
        phase_synchronies = [self.average_phase_synchrony(phases, query_phases) for _, phases in wavelet_transforms_and_phases]

        normalized_vec = self.normalize_vector(vec.flatten())
        normalized_vecs = [self.normalize_vector(v.flatten()) for v in vecs]
        cosine_similarities = [self.cosine_similarity(normalized_vec, v) for v in normalized_vecs]

        combined_scores = [ps * (0.5 * (cs + 1)) for ps, cs in zip(phase_synchronies, cosine_similarities)]
        return combined_scores