from setuptools import setup
setup(
    name='cli-anything-looker',
    version='1.0.0',
    packages=['cli_anything.looker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-looker=cli_anything.looker:cli']},
)
