from setuptools import setup
setup(
    name='cli-anything-light',
    version='1.0.0',
    packages=['cli_anything.light'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-light=cli_anything.light:cli']},
)
