from setuptools import setup
setup(
    name='cli-anything-presentation',
    version='1.0.0',
    packages=['cli_anything.presentation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-presentation=cli_anything.presentation:cli']},
)
