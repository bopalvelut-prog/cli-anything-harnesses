from setuptools import setup
setup(
    name='cli-anything-sharp',
    version='1.0.0',
    packages=['cli_anything.sharp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sharp=cli_anything.sharp:cli']},
)
