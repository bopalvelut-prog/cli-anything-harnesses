from setuptools import setup
setup(
    name='cli-anything-prison',
    version='1.0.0',
    packages=['cli_anything.prison'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prison=cli_anything.prison:cli']},
)
