from setuptools import setup
setup(
    name='cli-anything-oleg',
    version='1.0.0',
    packages=['cli_anything.oleg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oleg=cli_anything.oleg:cli']},
)
