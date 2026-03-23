from setuptools import setup
setup(
    name='cli-anything-sieve',
    version='1.0.0',
    packages=['cli_anything.sieve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sieve=cli_anything.sieve:cli']},
)
