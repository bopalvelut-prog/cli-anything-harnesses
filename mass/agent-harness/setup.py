from setuptools import setup
setup(
    name='cli-anything-mass',
    version='1.0.0',
    packages=['cli_anything.mass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mass=cli_anything.mass:cli']},
)
