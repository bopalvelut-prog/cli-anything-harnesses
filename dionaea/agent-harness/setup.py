from setuptools import setup
setup(
    name='cli-anything-dionaea',
    version='1.0.0',
    packages=['cli_anything.dionaea'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dionaea=cli_anything.dionaea:cli']},
)
