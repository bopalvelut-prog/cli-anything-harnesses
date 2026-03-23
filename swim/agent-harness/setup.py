from setuptools import setup
setup(
    name='cli-anything-swim',
    version='1.0.0',
    packages=['cli_anything.swim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-swim=cli_anything.swim:cli']},
)
