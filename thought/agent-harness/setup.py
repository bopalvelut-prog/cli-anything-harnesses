from setuptools import setup
setup(
    name='cli-anything-thought',
    version='1.0.0',
    packages=['cli_anything.thought'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thought=cli_anything.thought:cli']},
)
