from setuptools import setup
setup(
    name='cli-anything-screen',
    version='1.0.0',
    packages=['cli_anything.screen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-screen=cli_anything.screen:cli']},
)
