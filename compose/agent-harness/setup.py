from setuptools import setup
setup(
    name='cli-anything-compose',
    version='1.0.0',
    packages=['cli_anything.compose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-compose=cli_anything.compose:cli']},
)
