from setuptools import setup
setup(
    name='cli-anything-distance',
    version='1.0.0',
    packages=['cli_anything.distance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-distance=cli_anything.distance:cli']},
)
