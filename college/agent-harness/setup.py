from setuptools import setup
setup(
    name='cli-anything-college',
    version='1.0.0',
    packages=['cli_anything.college'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-college=cli_anything.college:cli']},
)
