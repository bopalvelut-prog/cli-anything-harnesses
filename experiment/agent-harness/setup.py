from setuptools import setup
setup(
    name='cli-anything-experiment',
    version='1.0.0',
    packages=['cli_anything.experiment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-experiment=cli_anything.experiment:cli']},
)
