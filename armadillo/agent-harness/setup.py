from setuptools import setup
setup(
    name='cli-anything-armadillo',
    version='1.0.0',
    packages=['cli_anything.armadillo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-armadillo=cli_anything.armadillo:cli']},
)
