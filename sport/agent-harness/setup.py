from setuptools import setup
setup(
    name='cli-anything-sport',
    version='1.0.0',
    packages=['cli_anything.sport'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sport=cli_anything.sport:cli']},
)
