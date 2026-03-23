from setuptools import setup
setup(
    name='cli-anything-logdna',
    version='1.0.0',
    packages=['cli_anything.logdna'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logdna=cli_anything.logdna:cli']},
)
