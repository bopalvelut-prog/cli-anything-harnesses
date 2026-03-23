from setuptools import setup
setup(
    name='cli-anything-strong',
    version='1.0.0',
    packages=['cli_anything.strong'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strong=cli_anything.strong:cli']},
)
