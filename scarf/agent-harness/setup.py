from setuptools import setup
setup(
    name='cli-anything-scarf',
    version='1.0.0',
    packages=['cli_anything.scarf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scarf=cli_anything.scarf:cli']},
)
