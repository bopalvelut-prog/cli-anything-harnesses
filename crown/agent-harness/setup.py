from setuptools import setup
setup(
    name='cli-anything-crown',
    version='1.0.0',
    packages=['cli_anything.crown'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crown=cli_anything.crown:cli']},
)
