from setuptools import setup
setup(
    name='cli-anything-pinia',
    version='1.0.0',
    packages=['cli_anything.pinia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pinia=cli_anything.pinia:cli']},
)
