from setuptools import setup
setup(
    name='cli-anything-burpsuite',
    version='1.0.0',
    packages=['cli_anything.burpsuite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-burpsuite=cli_anything.burpsuite:cli']},
)
