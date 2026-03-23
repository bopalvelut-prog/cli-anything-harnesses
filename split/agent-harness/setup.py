from setuptools import setup
setup(
    name='cli-anything-split',
    version='1.0.0',
    packages=['cli_anything.split'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-split=cli_anything.split:cli']},
)
