from setuptools import setup
setup(
    name='cli-anything-noise',
    version='1.0.0',
    packages=['cli_anything.noise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-noise=cli_anything.noise:cli']},
)
