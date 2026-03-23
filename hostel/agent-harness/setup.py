from setuptools import setup
setup(
    name='cli-anything-hostel',
    version='1.0.0',
    packages=['cli_anything.hostel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hostel=cli_anything.hostel:cli']},
)
