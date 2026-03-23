from setuptools import setup
setup(
    name='cli-anything-faith',
    version='1.0.0',
    packages=['cli_anything.faith'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-faith=cli_anything.faith:cli']},
)
