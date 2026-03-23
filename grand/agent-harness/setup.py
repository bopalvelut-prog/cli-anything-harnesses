from setuptools import setup
setup(
    name='cli-anything-grand',
    version='1.0.0',
    packages=['cli_anything.grand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grand=cli_anything.grand:cli']},
)
