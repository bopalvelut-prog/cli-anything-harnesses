from setuptools import setup
setup(
    name='cli-anything-sand',
    version='1.0.0',
    packages=['cli_anything.sand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sand=cli_anything.sand:cli']},
)
