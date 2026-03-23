from setuptools import setup
setup(
    name='cli-anything-anbox',
    version='1.0.0',
    packages=['cli_anything.anbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anbox=cli_anything.anbox:cli']},
)
