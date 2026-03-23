from setuptools import setup
setup(
    name='cli-anything-drink',
    version='1.0.0',
    packages=['cli_anything.drink'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drink=cli_anything.drink:cli']},
)
