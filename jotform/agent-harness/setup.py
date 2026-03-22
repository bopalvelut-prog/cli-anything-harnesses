from setuptools import setup
setup(
    name='cli-anything-jotform',
    version='1.0.0',
    packages=['cli_anything.jotform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jotform=cli_anything.jotform:cli']},
)
