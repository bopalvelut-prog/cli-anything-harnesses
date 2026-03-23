from setuptools import setup
setup(
    name='cli-anything-call',
    version='1.0.0',
    packages=['cli_anything.call'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-call=cli_anything.call:cli']},
)
