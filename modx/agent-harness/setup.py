from setuptools import setup
setup(
    name='cli-anything-modx',
    version='1.0.0',
    packages=['cli_anything.modx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-modx=cli_anything.modx:cli']},
)
