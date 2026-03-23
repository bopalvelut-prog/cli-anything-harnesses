from setuptools import setup
setup(
    name='cli-anything-uber',
    version='1.0.0',
    packages=['cli_anything.uber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uber=cli_anything.uber:cli']},
)
