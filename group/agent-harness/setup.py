from setuptools import setup
setup(
    name='cli-anything-group',
    version='1.0.0',
    packages=['cli_anything.group'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-group=cli_anything.group:cli']},
)
