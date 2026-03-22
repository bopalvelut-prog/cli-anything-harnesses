from setuptools import setup
setup(
    name='cli-anything-arista',
    version='1.0.0',
    packages=['cli_anything.arista'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arista=cli_anything.arista:cli']},
)
