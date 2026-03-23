from setuptools import setup
setup(
    name='cli-anything-schema',
    version='1.0.0',
    packages=['cli_anything.schema'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-schema=cli_anything.schema:cli']},
)
