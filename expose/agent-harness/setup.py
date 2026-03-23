from setuptools import setup
setup(
    name='cli-anything-expose',
    version='1.0.0',
    packages=['cli_anything.expose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-expose=cli_anything.expose:cli']},
)
