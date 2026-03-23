from setuptools import setup
setup(
    name='cli-anything-joi',
    version='1.0.0',
    packages=['cli_anything.joi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-joi=cli_anything.joi:cli']},
)
