from setuptools import setup
setup(
    name='cli-anything-holy',
    version='1.0.0',
    packages=['cli_anything.holy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-holy=cli_anything.holy:cli']},
)
