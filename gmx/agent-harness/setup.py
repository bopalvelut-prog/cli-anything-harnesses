from setuptools import setup
setup(
    name='cli-anything-gmx',
    version='1.0.0',
    packages=['cli_anything.gmx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gmx=cli_anything.gmx:cli']},
)
