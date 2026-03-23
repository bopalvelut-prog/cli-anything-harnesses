from setuptools import setup
setup(
    name='cli-anything-hunt',
    version='1.0.0',
    packages=['cli_anything.hunt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hunt=cli_anything.hunt:cli']},
)
