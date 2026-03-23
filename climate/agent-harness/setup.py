from setuptools import setup
setup(
    name='cli-anything-climate',
    version='1.0.0',
    packages=['cli_anything.climate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-climate=cli_anything.climate:cli']},
)
