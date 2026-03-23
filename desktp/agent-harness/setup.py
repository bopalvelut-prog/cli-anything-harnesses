from setuptools import setup
setup(
    name='cli-anything-desktp',
    version='1.0.0',
    packages=['cli_anything.desktp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-desktp=cli_anything.desktp:cli']},
)
