from setuptools import setup
setup(
    name='cli-anything-wraith',
    version='1.0.0',
    packages=['cli_anything.wraith'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wraith=cli_anything.wraith:cli']},
)
