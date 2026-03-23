from setuptools import setup
setup(
    name='cli-anything-timing',
    version='1.0.0',
    packages=['cli_anything.timing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timing=cli_anything.timing:cli']},
)
