from setuptools import setup
setup(
    name='cli-anything-satisfy',
    version='1.0.0',
    packages=['cli_anything.satisfy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-satisfy=cli_anything.satisfy:cli']},
)
