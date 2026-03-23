from setuptools import setup
setup(
    name='cli-anything-warrant',
    version='1.0.0',
    packages=['cli_anything.warrant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warrant=cli_anything.warrant:cli']},
)
