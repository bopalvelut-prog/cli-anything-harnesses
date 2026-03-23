from setuptools import setup
setup(
    name='cli-anything-what',
    version='1.0.0',
    packages=['cli_anything.what'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-what=cli_anything.what:cli']},
)
