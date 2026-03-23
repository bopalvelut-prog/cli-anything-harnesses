from setuptools import setup
setup(
    name='cli-anything-unusual',
    version='1.0.0',
    packages=['cli_anything.unusual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unusual=cli_anything.unusual:cli']},
)
