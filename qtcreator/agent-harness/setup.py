from setuptools import setup
setup(
    name='cli-anything-qtcreator',
    version='1.0.0',
    packages=['cli_anything.qtcreator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qtcreator=cli_anything.qtcreator:cli']},
)
