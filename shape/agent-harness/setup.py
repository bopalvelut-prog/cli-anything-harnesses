from setuptools import setup
setup(
    name='cli-anything-shape',
    version='1.0.0',
    packages=['cli_anything.shape'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shape=cli_anything.shape:cli']},
)
