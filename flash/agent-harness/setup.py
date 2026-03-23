from setuptools import setup
setup(
    name='cli-anything-flash',
    version='1.0.0',
    packages=['cli_anything.flash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flash=cli_anything.flash:cli']},
)
