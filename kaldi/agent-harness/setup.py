from setuptools import setup
setup(
    name='cli-anything-kaldi',
    version='1.0.0',
    packages=['cli_anything.kaldi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kaldi=cli_anything.kaldi:cli']},
)
