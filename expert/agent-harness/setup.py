from setuptools import setup
setup(
    name='cli-anything-expert',
    version='1.0.0',
    packages=['cli_anything.expert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-expert=cli_anything.expert:cli']},
)
