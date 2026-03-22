from setuptools import setup
setup(
    name='cli-anything-xxd',
    version='1.0.0',
    packages=['cli_anything.xxd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xxd=cli_anything.xxd:cli']},
)
