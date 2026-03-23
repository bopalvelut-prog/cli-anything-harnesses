from setuptools import setup
setup(
    name='cli-anything-national',
    version='1.0.0',
    packages=['cli_anything.national'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-national=cli_anything.national:cli']},
)
