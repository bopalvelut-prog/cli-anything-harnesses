from setuptools import setup
setup(
    name='cli-anything-software',
    version='1.0.0',
    packages=['cli_anything.software'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-software=cli_anything.software:cli']},
)
