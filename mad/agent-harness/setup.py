from setuptools import setup
setup(
    name='cli-anything-mad',
    version='1.0.0',
    packages=['cli_anything.mad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mad=cli_anything.mad:cli']},
)
