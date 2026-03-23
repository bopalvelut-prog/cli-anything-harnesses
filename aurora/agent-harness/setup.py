from setuptools import setup
setup(
    name='cli-anything-aurora',
    version='1.0.0',
    packages=['cli_anything.aurora'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aurora=cli_anything.aurora:cli']},
)
