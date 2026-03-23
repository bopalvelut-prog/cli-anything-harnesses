from setuptools import setup
setup(
    name='cli-anything-watchtower',
    version='1.0.0',
    packages=['cli_anything.watchtower'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-watchtower=cli_anything.watchtower:cli']},
)
