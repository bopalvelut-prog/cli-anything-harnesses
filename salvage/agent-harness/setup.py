from setuptools import setup
setup(
    name='cli-anything-salvage',
    version='1.0.0',
    packages=['cli_anything.salvage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-salvage=cli_anything.salvage:cli']},
)
