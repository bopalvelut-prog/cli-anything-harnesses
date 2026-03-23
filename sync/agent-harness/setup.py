from setuptools import setup
setup(
    name='cli-anything-sync',
    version='1.0.0',
    packages=['cli_anything.sync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sync=cli_anything.sync:cli']},
)
