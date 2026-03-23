from setuptools import setup
setup(
    name='cli-anything-thermal',
    version='1.0.0',
    packages=['cli_anything.thermal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thermal=cli_anything.thermal:cli']},
)
