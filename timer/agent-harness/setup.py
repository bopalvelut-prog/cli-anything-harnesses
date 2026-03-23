from setuptools import setup
setup(
    name='cli-anything-timer',
    version='1.0.0',
    packages=['cli_anything.timer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timer=cli_anything.timer:cli']},
)
