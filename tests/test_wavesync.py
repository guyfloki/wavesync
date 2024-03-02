import unittest
import numpy as np
from wavesync.wavesync import WaveSync  

class TestWaveSync(unittest.TestCase):

    def setUp(self):
        self.ws = WaveSync()

    def test_normalize_vector(self):
        vec = np.array([1, 2, 3])
        normalized_vec = self.ws.normalize_vector(vec)
        expected_length = 1.0
        actual_length = np.linalg.norm(normalized_vec)
        self.assertAlmostEqual(expected_length, actual_length)

    def test_create_complex_vector(self):
        vec = np.array([1, 2, 3, 4])
        complex_vec = self.ws.create_complex_vector(vec)
        expected_complex_vec = np.array([1 + 2j, 3 + 4j])
        np.testing.assert_array_almost_equal(expected_complex_vec, complex_vec)

    def test_compute_wavelet_transform_and_phase(self):
        vec = np.random.rand(1024)
        coeffs, phases = self.ws.compute_wavelet_transform_and_phase(vec)
        self.assertTrue(len(coeffs) > 0)
        self.assertTrue(len(phases) > 0)

    def test_average_phase_synchrony(self):
        phases_x = [np.array([0, np.pi])]
        phases_y = [np.array([np.pi, 0])]
        synchrony = self.ws.average_phase_synchrony(phases_x, phases_y)
        self.assertAlmostEqual(synchrony, 0, places=1)

    def test_cosine_similarity(self):
        vec1 = np.array([1, 0, 0])
        vec2 = np.array([0, 1, 0])
        similarity = self.ws.cosine_similarity(vec1, vec2)
        self.assertEqual(similarity, 0.0)

    def test_compare(self):
        vec = np.random.rand(1024)
        vecs = np.random.rand(5, 1024)
        scores = self.ws.compare(vec, vecs)
        self.assertEqual(len(scores), len(vecs))
        for score in scores:
            self.assertTrue(0 <= score <= 1)

if __name__ == '__main__':
    unittest.main()
