from setuptools import setup
setup(
    name='cli-anything-antenna',
    version='1.0.0',
    packages=['cli_anything.antenna'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-antenna=cli_anything.antenna:cli']},
)
