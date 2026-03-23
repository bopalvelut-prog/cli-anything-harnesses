from setuptools import setup
setup(
    name='cli-anything-sentence',
    version='1.0.0',
    packages=['cli_anything.sentence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sentence=cli_anything.sentence:cli']},
)
