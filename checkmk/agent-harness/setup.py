from setuptools import setup
setup(
    name='cli-anything-checkmk',
    version='1.0.0',
    packages=['cli_anything.checkmk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-checkmk=cli_anything.checkmk:cli']},
)
