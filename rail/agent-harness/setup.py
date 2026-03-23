from setuptools import setup
setup(
    name='cli-anything-rail',
    version='1.0.0',
    packages=['cli_anything.rail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rail=cli_anything.rail:cli']},
)
