from setuptools import setup
setup(
    name='cli-anything-line',
    version='1.0.0',
    packages=['cli_anything.line'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-line=cli_anything.line:cli']},
)
