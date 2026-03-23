from setuptools import setup
setup(
    name='cli-anything-smooth',
    version='1.0.0',
    packages=['cli_anything.smooth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smooth=cli_anything.smooth:cli']},
)
