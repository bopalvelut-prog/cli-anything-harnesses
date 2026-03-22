from setuptools import setup
setup(
    name='cli-anything-zapier',
    version='1.0.0',
    packages=['cli_anything.zapier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zapier=cli_anything.zapier:cli']},
)
