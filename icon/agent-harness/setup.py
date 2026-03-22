from setuptools import setup
setup(
    name='cli-anything-icon',
    version='1.0.0',
    packages=['cli_anything.icon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-icon=cli_anything.icon:cli']},
)
