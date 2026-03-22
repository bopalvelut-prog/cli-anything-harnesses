from setuptools import setup
setup(
    name='cli-anything-carbonite',
    version='1.0.0',
    packages=['cli_anything.carbonite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-carbonite=cli_anything.carbonite:cli']},
)
