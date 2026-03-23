from setuptools import setup
setup(
    name='cli-anything-bandage',
    version='1.0.0',
    packages=['cli_anything.bandage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bandage=cli_anything.bandage:cli']},
)
