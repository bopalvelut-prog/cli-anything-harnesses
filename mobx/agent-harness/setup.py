from setuptools import setup
setup(
    name='cli-anything-mobx',
    version='1.0.0',
    packages=['cli_anything.mobx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mobx=cli_anything.mobx:cli']},
)
