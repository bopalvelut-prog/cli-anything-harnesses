from setuptools import setup
setup(
    name='cli-anything-local',
    version='1.0.0',
    packages=['cli_anything.local'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-local=cli_anything.local:cli']},
)
