from setuptools import setup
setup(
    name='cli-anything-portainer',
    version='1.0.0',
    packages=['cli_anything.portainer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-portainer=cli_anything.portainer:cli']},
)
