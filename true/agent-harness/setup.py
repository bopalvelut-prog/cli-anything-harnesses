from setuptools import setup
setup(
    name='cli-anything-true',
    version='1.0.0',
    packages=['cli_anything.true'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-true=cli_anything.true:cli']},
)
