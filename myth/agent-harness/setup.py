from setuptools import setup
setup(
    name='cli-anything-myth',
    version='1.0.0',
    packages=['cli_anything.myth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-myth=cli_anything.myth:cli']},
)
