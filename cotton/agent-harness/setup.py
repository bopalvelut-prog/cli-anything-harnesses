from setuptools import setup
setup(
    name='cli-anything-cotton',
    version='1.0.0',
    packages=['cli_anything.cotton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cotton=cli_anything.cotton:cli']},
)
