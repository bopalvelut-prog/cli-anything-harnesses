from setuptools import setup
setup(
    name='cli-anything-json',
    version='1.0.0',
    packages=['cli_anything.json'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-json=cli_anything.json:cli']},
)
