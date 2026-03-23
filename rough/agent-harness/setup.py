from setuptools import setup
setup(
    name='cli-anything-rough',
    version='1.0.0',
    packages=['cli_anything.rough'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rough=cli_anything.rough:cli']},
)
