from setuptools import setup
setup(
    name='cli-anything-pirate',
    version='1.0.0',
    packages=['cli_anything.pirate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pirate=cli_anything.pirate:cli']},
)
