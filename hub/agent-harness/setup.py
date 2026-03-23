from setuptools import setup
setup(
    name='cli-anything-hub',
    version='1.0.0',
    packages=['cli_anything.hub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hub=cli_anything.hub:cli']},
)
