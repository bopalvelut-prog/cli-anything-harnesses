from setuptools import setup
setup(
    name='cli-anything-restart',
    version='1.0.0',
    packages=['cli_anything.restart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restart=cli_anything.restart:cli']},
)
