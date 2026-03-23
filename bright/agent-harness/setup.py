from setuptools import setup
setup(
    name='cli-anything-bright',
    version='1.0.0',
    packages=['cli_anything.bright'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bright=cli_anything.bright:cli']},
)
