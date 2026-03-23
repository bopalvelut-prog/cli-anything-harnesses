from setuptools import setup
setup(
    name='cli-anything-planning',
    version='1.0.0',
    packages=['cli_anything.planning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-planning=cli_anything.planning:cli']},
)
