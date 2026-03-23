from setuptools import setup
setup(
    name='cli-anything-fair',
    version='1.0.0',
    packages=['cli_anything.fair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fair=cli_anything.fair:cli']},
)
