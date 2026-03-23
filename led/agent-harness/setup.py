from setuptools import setup
setup(
    name='cli-anything-led',
    version='1.0.0',
    packages=['cli_anything.led'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-led=cli_anything.led:cli']},
)
