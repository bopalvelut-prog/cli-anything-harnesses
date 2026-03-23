from setuptools import setup
setup(
    name='cli-anything-extend',
    version='1.0.0',
    packages=['cli_anything.extend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-extend=cli_anything.extend:cli']},
)
