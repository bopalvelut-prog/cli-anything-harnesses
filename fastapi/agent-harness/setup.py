from setuptools import setup
setup(
    name='cli-anything-fastapi',
    version='1.0.0',
    packages=['cli_anything.fastapi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fastapi=cli_anything.fastapi:cli']},
)
