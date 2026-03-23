from setuptools import setup
setup(
    name='cli-anything-nx',
    version='1.0.0',
    packages=['cli_anything.nx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nx=cli_anything.nx:cli']},
)
