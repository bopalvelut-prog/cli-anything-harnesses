from setuptools import setup
setup(
    name='cli-anything-composable',
    version='1.0.0',
    packages=['cli_anything.composable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-composable=cli_anything.composable:cli']},
)
