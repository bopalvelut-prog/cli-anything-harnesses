from setuptools import setup
setup(
    name='cli-anything-tau',
    version='1.0.0',
    packages=['cli_anything.tau'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tau=cli_anything.tau:cli']},
)
