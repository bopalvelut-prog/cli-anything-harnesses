from setuptools import setup
setup(
    name='cli-anything-anonymous',
    version='1.0.0',
    packages=['cli_anything.anonymous'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anonymous=cli_anything.anonymous:cli']},
)
