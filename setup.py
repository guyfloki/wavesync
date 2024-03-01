from setuptools import setup, find_packages

setup(
    name='wavesync',
    version='0.1.0',
    author='Liubomyr Horbatko',
    author_email='liubomir.horbatko@gmail.com',
    packages=find_packages(),
    description='A Python package for wavelet-based signal synchronization analysis',
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
