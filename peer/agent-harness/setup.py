from setuptools import setup
setup(
    name='cli-anything-peer',
    version='1.0.0',
    packages=['cli_anything.peer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peer=cli_anything.peer:cli']},
)
