from setuptools import setup
setup(
    name='cli-anything-scale',
    version='1.0.0',
    packages=['cli_anything.scale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scale=cli_anything.scale:cli']},
)
