from setuptools import setup
setup(
    name='cli-anything-quantum',
    version='1.0.0',
    packages=['cli_anything.quantum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quantum=cli_anything.quantum:cli']},
)
