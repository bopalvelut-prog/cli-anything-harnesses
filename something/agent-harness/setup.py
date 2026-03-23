from setuptools import setup
setup(
    name='cli-anything-something',
    version='1.0.0',
    packages=['cli_anything.something'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-something=cli_anything.something:cli']},
)
