from setuptools import setup
setup(
    name='cli-anything-ship',
    version='1.0.0',
    packages=['cli_anything.ship'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ship=cli_anything.ship:cli']},
)
