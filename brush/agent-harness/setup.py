from setuptools import setup
setup(
    name='cli-anything-brush',
    version='1.0.0',
    packages=['cli_anything.brush'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brush=cli_anything.brush:cli']},
)
