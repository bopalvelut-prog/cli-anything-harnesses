from setuptools import setup
setup(
    name='cli-anything-pyo3',
    version='1.0.0',
    packages=['cli_anything.pyo3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyo3=cli_anything.pyo3:cli']},
)
