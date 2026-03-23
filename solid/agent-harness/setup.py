from setuptools import setup
setup(
    name='cli-anything-solid',
    version='1.0.0',
    packages=['cli_anything.solid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solid=cli_anything.solid:cli']},
)
