from setuptools import setup
setup(
    name='cli-anything-haiku',
    version='1.0.0',
    packages=['cli_anything.haiku'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-haiku=cli_anything.haiku:cli']},
)
