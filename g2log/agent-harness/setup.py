from setuptools import setup
setup(
    name='cli-anything-g2log',
    version='1.0.0',
    packages=['cli_anything.g2log'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-g2log=cli_anything.g2log:cli']},
)
