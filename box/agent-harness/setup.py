from setuptools import setup
setup(
    name='cli-anything-box',
    version='1.0.0',
    packages=['cli_anything.box'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-box=cli_anything.box:cli']},
)
