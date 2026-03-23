from setuptools import setup
setup(
    name='cli-anything-miracle',
    version='1.0.0',
    packages=['cli_anything.miracle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-miracle=cli_anything.miracle:cli']},
)
