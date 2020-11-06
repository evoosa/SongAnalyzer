from distutils.core import setup

setup(
    name='song_analyzer',
    version='1.0.0',
    install_requires=[
        'textblob==0.15.3',
        #'textblob.download_corpora' # FIXME ? its a module?
    ],
    author='evoosa',
    description='feed it with lyrics and get some valuable data about it'
)
