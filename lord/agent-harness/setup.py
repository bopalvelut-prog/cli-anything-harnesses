from setuptools import setup
setup(
    name='cli-anything-lord',
    version='1.0.0',
    packages=['cli_anything.lord'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lord=cli_anything.lord:cli']},
)
