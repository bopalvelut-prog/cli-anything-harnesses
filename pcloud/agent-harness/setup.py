from setuptools import setup
setup(
    name='cli-anything-pcloud',
    version='1.0.0',
    packages=['cli_anything.pcloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pcloud=cli_anything.pcloud:cli']},
)
