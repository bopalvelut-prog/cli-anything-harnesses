from setuptools import setup
setup(
    name='cli-anything-allennlp',
    version='1.0.0',
    packages=['cli_anything.allennlp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-allennlp=cli_anything.allennlp:cli']},
)
