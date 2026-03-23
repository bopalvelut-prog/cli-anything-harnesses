from setuptools import setup
setup(
    name='cli-anything-swear',
    version='1.0.0',
    packages=['cli_anything.swear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-swear=cli_anything.swear:cli']},
)
