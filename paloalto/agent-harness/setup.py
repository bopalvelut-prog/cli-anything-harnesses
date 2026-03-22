from setuptools import setup
setup(
    name='cli-anything-paloalto',
    version='1.0.0',
    packages=['cli_anything.paloalto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paloalto=cli_anything.paloalto:cli']},
)
