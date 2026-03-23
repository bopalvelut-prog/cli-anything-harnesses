from setuptools import setup
setup(
    name='cli-anything-diesel',
    version='1.0.0',
    packages=['cli_anything.diesel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-diesel=cli_anything.diesel:cli']},
)
