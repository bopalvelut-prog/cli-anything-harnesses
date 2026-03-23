from setuptools import setup
setup(
    name='cli-anything-marko',
    version='1.0.0',
    packages=['cli_anything.marko'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marko=cli_anything.marko:cli']},
)
