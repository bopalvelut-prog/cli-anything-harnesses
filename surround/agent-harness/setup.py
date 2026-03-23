from setuptools import setup
setup(
    name='cli-anything-surround',
    version='1.0.0',
    packages=['cli_anything.surround'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-surround=cli_anything.surround:cli']},
)
