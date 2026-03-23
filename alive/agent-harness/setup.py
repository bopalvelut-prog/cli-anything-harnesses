from setuptools import setup
setup(
    name='cli-anything-alive',
    version='1.0.0',
    packages=['cli_anything.alive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alive=cli_anything.alive:cli']},
)
