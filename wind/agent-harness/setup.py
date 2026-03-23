from setuptools import setup
setup(
    name='cli-anything-wind',
    version='1.0.0',
    packages=['cli_anything.wind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wind=cli_anything.wind:cli']},
)
