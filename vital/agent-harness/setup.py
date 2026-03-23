from setuptools import setup
setup(
    name='cli-anything-vital',
    version='1.0.0',
    packages=['cli_anything.vital'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vital=cli_anything.vital:cli']},
)
