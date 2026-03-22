from setuptools import setup
setup(
    name='cli-anything-dagda',
    version='1.0.0',
    packages=['cli_anything.dagda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dagda=cli_anything.dagda:cli']},
)
