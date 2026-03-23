from setuptools import setup
setup(
    name='cli-anything-masstransit',
    version='1.0.0',
    packages=['cli_anything.masstransit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-masstransit=cli_anything.masstransit:cli']},
)
