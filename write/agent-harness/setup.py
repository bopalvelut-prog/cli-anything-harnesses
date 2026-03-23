from setuptools import setup
setup(
    name='cli-anything-write',
    version='1.0.0',
    packages=['cli_anything.write'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-write=cli_anything.write:cli']},
)
