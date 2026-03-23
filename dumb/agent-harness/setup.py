from setuptools import setup
setup(
    name='cli-anything-dumb',
    version='1.0.0',
    packages=['cli_anything.dumb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dumb=cli_anything.dumb:cli']},
)
