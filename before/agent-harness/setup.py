from setuptools import setup
setup(
    name='cli-anything-before',
    version='1.0.0',
    packages=['cli_anything.before'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-before=cli_anything.before:cli']},
)
