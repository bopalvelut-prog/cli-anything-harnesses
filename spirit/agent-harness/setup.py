from setuptools import setup
setup(
    name='cli-anything-spirit',
    version='1.0.0',
    packages=['cli_anything.spirit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spirit=cli_anything.spirit:cli']},
)
