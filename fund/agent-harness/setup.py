from setuptools import setup
setup(
    name='cli-anything-fund',
    version='1.0.0',
    packages=['cli_anything.fund'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fund=cli_anything.fund:cli']},
)
