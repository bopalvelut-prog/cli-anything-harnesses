from setuptools import setup
setup(
    name='cli-anything-travel',
    version='1.0.0',
    packages=['cli_anything.travel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-travel=cli_anything.travel:cli']},
)
