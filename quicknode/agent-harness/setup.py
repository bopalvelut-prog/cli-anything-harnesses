from setuptools import setup
setup(
    name='cli-anything-quicknode',
    version='1.0.0',
    packages=['cli_anything.quicknode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quicknode=cli_anything.quicknode:cli']},
)
