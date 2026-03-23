from setuptools import setup
setup(
    name='cli-anything-stream',
    version='1.0.0',
    packages=['cli_anything.stream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stream=cli_anything.stream:cli']},
)
