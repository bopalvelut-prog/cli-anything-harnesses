from setuptools import setup
setup(
    name='cli-anything-bottom',
    version='1.0.0',
    packages=['cli_anything.bottom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bottom=cli_anything.bottom:cli']},
)
