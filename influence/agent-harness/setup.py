from setuptools import setup
setup(
    name='cli-anything-influence',
    version='1.0.0',
    packages=['cli_anything.influence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-influence=cli_anything.influence:cli']},
)
