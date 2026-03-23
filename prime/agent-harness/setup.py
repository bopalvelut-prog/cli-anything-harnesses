from setuptools import setup
setup(
    name='cli-anything-prime',
    version='1.0.0',
    packages=['cli_anything.prime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prime=cli_anything.prime:cli']},
)
