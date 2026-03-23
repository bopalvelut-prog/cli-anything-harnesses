from setuptools import setup
setup(
    name='cli-anything-eager',
    version='1.0.0',
    packages=['cli_anything.eager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eager=cli_anything.eager:cli']},
)
