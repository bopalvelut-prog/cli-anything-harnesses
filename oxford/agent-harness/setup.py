from setuptools import setup
setup(
    name='cli-anything-oxford',
    version='1.0.0',
    packages=['cli_anything.oxford'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oxford=cli_anything.oxford:cli']},
)
