from setuptools import setup
setup(
    name='cli-anything-elect',
    version='1.0.0',
    packages=['cli_anything.elect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elect=cli_anything.elect:cli']},
)
