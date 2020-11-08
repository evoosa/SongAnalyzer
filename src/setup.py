import setuptools

setuptools.setup(
    name='song_analyzer',
    version='1.0.0',
    install_requires=[
        'textblob==0.15.3',
        'pandas==1.1.4',
        'matplotlib==3.3.1',
        'numpy==1.19.3'
    ],
    author='evoosa',
    description='feed it with lyrics and get some valuable data about it'
)
