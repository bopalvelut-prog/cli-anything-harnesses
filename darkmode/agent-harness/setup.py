from setuptools import setup
setup(
    name='cli-anything-darkmode',
    version='1.0.0',
    packages=['cli_anything.darkmode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-darkmode=cli_anything.darkmode:cli']},
)
