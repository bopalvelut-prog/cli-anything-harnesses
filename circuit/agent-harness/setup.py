from setuptools import setup
setup(
    name='cli-anything-circuit',
    version='1.0.0',
    packages=['cli_anything.circuit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-circuit=cli_anything.circuit:cli']},
)
