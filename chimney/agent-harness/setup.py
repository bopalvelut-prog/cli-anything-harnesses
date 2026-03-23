from setuptools import setup
setup(
    name='cli-anything-chimney',
    version='1.0.0',
    packages=['cli_anything.chimney'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chimney=cli_anything.chimney:cli']},
)
