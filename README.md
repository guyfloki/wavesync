
WaveSync is a Python library crafted for the analysis of vectors and embeddings, specifically tailored for use in Retrieval-Augmented Generation (RAG) systems. 

Unlike traditional methods that rely on cosine similarity for embeddings comparison, WaveSync introduces a novel approach by employing time series decomposition and phase analysis. This method enables the library to perform a more nuanced, nonlinear, and rapid analysis of embeddings, allowing for the identification of deeper similarities and differences beyond what cosine similarity can offer.

## Installation

### Required Libraries

Before installing WaveSync, you have to ensure the following libraries are already installed on your system:

![NumPy Badge](https://img.shields.io/badge/NumPy-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white) 
```bash
pip install numpy
```

![PyWavelets Badge](https://img.shields.io/badge/PyWavelets-%23013243.svg?&style=for-the-badge&logo=pywavelets&logoColor=white)
```bash
pip install PyWavelets
```

### Installation WaveSync


```bash
pip install PyWaveSync
```

## Usage

For quick start:

```python
from wavesync.wavesync import WaveSync
import numpy as np

vec = np.random.rand(1024)  
vecs = np.random.rand(10, 1024)

ws = WaveSync()

wavesync_scores = ws.compare(vec, vecs)

print(wavesync_scores)
```

If you want to see how the algorithm works on different types of vectors:

```python
from wavesync.wavesync import WaveSync
import numpy as np

ws = WaveSync()

np.random.seed(42)  
vec = np.random.rand(1024)  
similar_vecs = [vec + np.random.normal(0, 0.01, len(vec)) for _ in range(5)]
dissimilar_vecs = [np.random.rand(len(vec)) for _ in range(5)]
vec_a = np.random.rand(1024)
vec_b = -vec_a  # Coordinate-wise opposite of vec_a

# Test with similar, dissimilar, and opposite vectors
wavesync_similar_scores = ws.compare(vec, similar_vecs)
wavesync_dissimilar_scores = ws.compare(vec, dissimilar_vecs)
wavesync_opposite_scores = ws.compare(vec_a, [vec_b])

print(wavesync_similar_scores, wavesync_dissimilar_scores, wavesync_opposite_scores)
```

## Learn More

For those interested in diving deeper into how the WaveSync algorithm works, detailed explanations and use cases can be found on the following platforms:

- **English** (**Will be available in approximately 3 days**): Check out our articles on [Medium](https://medium.com) for an in-depth look at WaveSync. 
- **Russian** (**Will be available in approximately 2 days**): For Russian speakers, detailed discussions can be found on [Habr](https://habr.com).

## Community and Contact

I'm looking forward to collaborating with anyone interested in improving WaveSync. Your feedback, suggestions, and contributions are always welcome.

### How to Contribute

- **Contributions**: If you'd like to contribute, start by forking the repository on GitHub. Then, create a new branch for your feature or bug fix, make your changes, and test them. When you're ready, submit a pull request with a detailed description of your work.

- **Feedback and Discussions**: For comments, questions, or suggestions, please use [GitHub Issues](https://github.com/guyfloki/wavesync/issues). It's a great way to provide feedback or start a conversation about the library.

### Direct Contact

- If you have specific inquiries or ideas you'd prefer to discuss directly, you can reach out to me via email at [liubomir.horbatko@gmail.com](mailto:liubomir.horbatko@gmail.com). I'm always open to hearing from users and potential collaborators.

Your involvement is crucial for making WaveSync even better.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
