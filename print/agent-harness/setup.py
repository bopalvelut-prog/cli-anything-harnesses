from setuptools import setup
setup(
    name='cli-anything-print',
    version='1.0.0',
    packages=['cli_anything.print'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-print=cli_anything.print:cli']},
)
