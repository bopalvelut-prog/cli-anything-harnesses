from setuptools import setup
setup(
    name='cli-anything-each',
    version='1.0.0',
    packages=['cli_anything.each'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-each=cli_anything.each:cli']},
)
