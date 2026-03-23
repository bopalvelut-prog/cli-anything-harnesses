from setuptools import setup
setup(
    name='cli-anything-treasure',
    version='1.0.0',
    packages=['cli_anything.treasure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-treasure=cli_anything.treasure:cli']},
)
