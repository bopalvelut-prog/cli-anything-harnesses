from setuptools import setup
setup(
    name='cli-anything-check',
    version='1.0.0',
    packages=['cli_anything.check'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-check=cli_anything.check:cli']},
)
