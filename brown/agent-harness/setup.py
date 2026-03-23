from setuptools import setup
setup(
    name='cli-anything-brown',
    version='1.0.0',
    packages=['cli_anything.brown'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brown=cli_anything.brown:cli']},
)
