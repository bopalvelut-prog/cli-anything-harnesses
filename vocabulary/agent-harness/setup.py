from setuptools import setup
setup(
    name='cli-anything-vocabulary',
    version='1.0.0',
    packages=['cli_anything.vocabulary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vocabulary=cli_anything.vocabulary:cli']},
)
