from setuptools import setup
setup(
    name='cli-anything-flow',
    version='1.0.0',
    packages=['cli_anything.flow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flow=cli_anything.flow:cli']},
)
