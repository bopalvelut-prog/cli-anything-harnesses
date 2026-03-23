from setuptools import setup
setup(
    name='cli-anything-turf',
    version='1.0.0',
    packages=['cli_anything.turf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turf=cli_anything.turf:cli']},
)
