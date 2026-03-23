from setuptools import setup
setup(
    name='cli-anything-shiny',
    version='1.0.0',
    packages=['cli_anything.shiny'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shiny=cli_anything.shiny:cli']},
)
