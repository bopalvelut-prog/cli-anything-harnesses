from setuptools import setup
setup(
    name='cli-anything-crewai',
    version='1.0.0',
    packages=['cli_anything.crewai'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crewai=cli_anything.crewai:cli']},
)
