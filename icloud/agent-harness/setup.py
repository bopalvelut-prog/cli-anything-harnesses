from setuptools import setup
setup(
    name='cli-anything-icloud',
    version='1.0.0',
    packages=['cli_anything.icloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-icloud=cli_anything.icloud:cli']},
)
