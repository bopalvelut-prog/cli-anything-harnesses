from setuptools import setup
setup(
    name='cli-anything-purge',
    version='1.0.0',
    packages=['cli_anything.purge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-purge=cli_anything.purge:cli']},
)
