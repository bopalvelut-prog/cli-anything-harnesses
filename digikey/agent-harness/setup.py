from setuptools import setup
setup(
    name='cli-anything-digikey',
    version='1.0.0',
    packages=['cli_anything.digikey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-digikey=cli_anything.digikey:cli']},
)
