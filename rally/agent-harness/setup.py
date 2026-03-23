from setuptools import setup
setup(
    name='cli-anything-rally',
    version='1.0.0',
    packages=['cli_anything.rally'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rally=cli_anything.rally:cli']},
)
