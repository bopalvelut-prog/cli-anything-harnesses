from setuptools import setup
setup(
    name='cli-anything-pybind11',
    version='1.0.0',
    packages=['cli_anything.pybind11'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pybind11=cli_anything.pybind11:cli']},
)
