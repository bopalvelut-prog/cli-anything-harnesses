from setuptools import setup
setup(
    name='cli-anything-clockify',
    version='1.0.0',
    packages=['cli_anything.clockify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clockify=cli_anything.clockify:cli']},
)
