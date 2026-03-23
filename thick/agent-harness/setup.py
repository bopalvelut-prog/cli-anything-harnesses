from setuptools import setup
setup(
    name='cli-anything-thick',
    version='1.0.0',
    packages=['cli_anything.thick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thick=cli_anything.thick:cli']},
)
