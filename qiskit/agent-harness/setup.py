from setuptools import setup
setup(
    name='cli-anything-qiskit',
    version='1.0.0',
    packages=['cli_anything.qiskit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qiskit=cli_anything.qiskit:cli']},
)
