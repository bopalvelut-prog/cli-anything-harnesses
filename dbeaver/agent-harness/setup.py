from setuptools import setup
setup(
    name='cli-anything-dbeaver',
    version='1.0.0',
    packages=['cli_anything.dbeaver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dbeaver=cli_anything.dbeaver:cli']},
)
