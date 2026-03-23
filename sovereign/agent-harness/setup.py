from setuptools import setup
setup(
    name='cli-anything-sovereign',
    version='1.0.0',
    packages=['cli_anything.sovereign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sovereign=cli_anything.sovereign:cli']},
)
