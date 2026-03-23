from setuptools import setup
setup(
    name='cli-anything-debt',
    version='1.0.0',
    packages=['cli_anything.debt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-debt=cli_anything.debt:cli']},
)
