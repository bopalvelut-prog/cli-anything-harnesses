from setuptools import setup
setup(
    name='cli-anything-ready',
    version='1.0.0',
    packages=['cli_anything.ready'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ready=cli_anything.ready:cli']},
)
