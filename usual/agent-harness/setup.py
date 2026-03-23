from setuptools import setup
setup(
    name='cli-anything-usual',
    version='1.0.0',
    packages=['cli_anything.usual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-usual=cli_anything.usual:cli']},
)
