from setuptools import setup
setup(
    name='cli-anything-philosophy',
    version='1.0.0',
    packages=['cli_anything.philosophy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-philosophy=cli_anything.philosophy:cli']},
)
