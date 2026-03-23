from setuptools import setup
setup(
    name='cli-anything-compass',
    version='1.0.0',
    packages=['cli_anything.compass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-compass=cli_anything.compass:cli']},
)
