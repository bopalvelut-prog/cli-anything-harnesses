from setuptools import setup
setup(
    name='cli-anything-javac',
    version='1.0.0',
    packages=['cli_anything.javac'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-javac=cli_anything.javac:cli']},
)
