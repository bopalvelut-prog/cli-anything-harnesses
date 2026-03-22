from setuptools import setup
setup(
    name='cli-anything-hubstaff',
    version='1.0.0',
    packages=['cli_anything.hubstaff'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hubstaff=cli_anything.hubstaff:cli']},
)
