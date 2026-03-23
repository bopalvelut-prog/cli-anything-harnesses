from setuptools import setup
setup(
    name='cli-anything-marlin',
    version='1.0.0',
    packages=['cli_anything.marlin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marlin=cli_anything.marlin:cli']},
)
