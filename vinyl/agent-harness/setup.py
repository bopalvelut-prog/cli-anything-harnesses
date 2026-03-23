from setuptools import setup
setup(
    name='cli-anything-vinyl',
    version='1.0.0',
    packages=['cli_anything.vinyl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vinyl=cli_anything.vinyl:cli']},
)
