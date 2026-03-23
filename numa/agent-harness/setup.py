from setuptools import setup
setup(
    name='cli-anything-numa',
    version='1.0.0',
    packages=['cli_anything.numa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-numa=cli_anything.numa:cli']},
)
