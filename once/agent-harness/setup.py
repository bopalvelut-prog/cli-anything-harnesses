from setuptools import setup
setup(
    name='cli-anything-once',
    version='1.0.0',
    packages=['cli_anything.once'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-once=cli_anything.once:cli']},
)
