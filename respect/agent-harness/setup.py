from setuptools import setup
setup(
    name='cli-anything-respect',
    version='1.0.0',
    packages=['cli_anything.respect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-respect=cli_anything.respect:cli']},
)
