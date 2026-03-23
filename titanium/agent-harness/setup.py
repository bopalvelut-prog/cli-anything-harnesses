from setuptools import setup
setup(
    name='cli-anything-titanium',
    version='1.0.0',
    packages=['cli_anything.titanium'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-titanium=cli_anything.titanium:cli']},
)
