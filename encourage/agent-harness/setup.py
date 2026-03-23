from setuptools import setup
setup(
    name='cli-anything-encourage',
    version='1.0.0',
    packages=['cli_anything.encourage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-encourage=cli_anything.encourage:cli']},
)
