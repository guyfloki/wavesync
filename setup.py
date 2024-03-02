from setuptools import setup, find_packages

setup(
    name='PyWaveSync',
    version='0.1.1',
    author='Liubomyr Horbatko',
    author_email='liubomir.horbatko@gmail.com',
    packages=find_packages(),
    description='WaveSync is a Python library for nuanced, nonlinear, and rapid analysis of vectors and embeddings, tailored for RAG systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/guyfloki/wavesync',
    install_requires=[
        'numpy',
        'PyWavelets'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)