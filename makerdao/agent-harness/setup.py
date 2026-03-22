from setuptools import setup
setup(
    name='cli-anything-makerdao',
    version='1.0.0',
    packages=['cli_anything.makerdao'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-makerdao=cli_anything.makerdao:cli']},
)
