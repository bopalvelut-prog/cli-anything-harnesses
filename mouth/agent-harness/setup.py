from setuptools import setup
setup(
    name='cli-anything-mouth',
    version='1.0.0',
    packages=['cli_anything.mouth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mouth=cli_anything.mouth:cli']},
)
