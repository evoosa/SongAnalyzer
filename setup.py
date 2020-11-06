from distutils.core import setup

setup(
    name='song_analyzer',
    version='1.0.0',
    packages=['song_analyzer'],
    url='',
    install_requires=[
        'textblob==0.15.3',
        'textblob.download_corpora'
    ],
    author='evoosa',
    description='feed it with lyrics and get some valuable data about it'
)
