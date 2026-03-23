from setuptools import setup
setup(
    name='cli-anything-facility',
    version='1.0.0',
    packages=['cli_anything.facility'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-facility=cli_anything.facility:cli']},
)
