from setuptools import setup
setup(
    name='cli-anything-treat',
    version='1.0.0',
    packages=['cli_anything.treat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-treat=cli_anything.treat:cli']},
)
