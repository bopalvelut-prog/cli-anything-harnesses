from setuptools import setup
setup(
    name='cli-anything-panic',
    version='1.0.0',
    packages=['cli_anything.panic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-panic=cli_anything.panic:cli']},
)
