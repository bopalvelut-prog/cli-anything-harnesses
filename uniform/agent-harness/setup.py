from setuptools import setup
setup(
    name='cli-anything-uniform',
    version='1.0.0',
    packages=['cli_anything.uniform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uniform=cli_anything.uniform:cli']},
)
