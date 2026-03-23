from setuptools import setup
setup(
    name='cli-anything-static',
    version='1.0.0',
    packages=['cli_anything.static'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-static=cli_anything.static:cli']},
)
