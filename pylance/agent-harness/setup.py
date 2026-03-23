from setuptools import setup
setup(
    name='cli-anything-pylance',
    version='1.0.0',
    packages=['cli_anything.pylance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pylance=cli_anything.pylance:cli']},
)
