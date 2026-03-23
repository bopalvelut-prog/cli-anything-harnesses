from setuptools import setup
setup(
    name='cli-anything-morning',
    version='1.0.0',
    packages=['cli_anything.morning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-morning=cli_anything.morning:cli']},
)
