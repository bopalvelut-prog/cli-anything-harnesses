from setuptools import setup
setup(
    name='cli-anything-permanent',
    version='1.0.0',
    packages=['cli_anything.permanent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-permanent=cli_anything.permanent:cli']},
)
