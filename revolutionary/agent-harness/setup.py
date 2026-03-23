from setuptools import setup
setup(
    name='cli-anything-revolutionary',
    version='1.0.0',
    packages=['cli_anything.revolutionary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-revolutionary=cli_anything.revolutionary:cli']},
)
