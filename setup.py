from setuptools import setup

setup(
    name='keras-word-char-embd',
    version='0.15',
    packages=['keras_wc_embd'],
    url='https://github.com/CyberZHG/keras-word-char-embd',
    license='MIT',
    author='CyberZHG',
    author_email='CyberZHG@gmail.com',
    description='Concatenate word and character embeddings in Keras',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'keras',
    ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
