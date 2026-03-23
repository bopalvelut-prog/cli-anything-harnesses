from setuptools import setup
setup(
    name='cli-anything-turbo',
    version='1.0.0',
    packages=['cli_anything.turbo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turbo=cli_anything.turbo:cli']},
)
