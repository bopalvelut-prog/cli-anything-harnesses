from setuptools import setup
setup(
    name='cli-anything-tutorial',
    version='1.0.0',
    packages=['cli_anything.tutorial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tutorial=cli_anything.tutorial:cli']},
)
