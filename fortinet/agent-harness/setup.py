from setuptools import setup
setup(
    name='cli-anything-fortinet',
    version='1.0.0',
    packages=['cli_anything.fortinet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fortinet=cli_anything.fortinet:cli']},
)
