from setuptools import setup
setup(
    name='cli-anything-partner',
    version='1.0.0',
    packages=['cli_anything.partner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-partner=cli_anything.partner:cli']},
)
