from setuptools import setup
setup(
    name='cli-anything-i3',
    version='1.0.0',
    packages=['cli_anything.i3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-i3=cli_anything.i3:cli']},
)
