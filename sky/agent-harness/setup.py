from setuptools import setup
setup(
    name='cli-anything-sky',
    version='1.0.0',
    packages=['cli_anything.sky'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sky=cli_anything.sky:cli']},
)
