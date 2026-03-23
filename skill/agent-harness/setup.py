from setuptools import setup
setup(
    name='cli-anything-skill',
    version='1.0.0',
    packages=['cli_anything.skill'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skill=cli_anything.skill:cli']},
)
