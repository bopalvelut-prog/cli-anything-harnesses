from setuptools import setup
setup(
    name='cli-anything-tribe',
    version='1.0.0',
    packages=['cli_anything.tribe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tribe=cli_anything.tribe:cli']},
)
