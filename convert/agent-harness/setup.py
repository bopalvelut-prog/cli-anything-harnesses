from setuptools import setup
setup(
    name='cli-anything-convert',
    version='1.0.0',
    packages=['cli_anything.convert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-convert=cli_anything.convert:cli']},
)
