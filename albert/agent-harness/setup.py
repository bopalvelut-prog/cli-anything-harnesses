from setuptools import setup
setup(
    name='cli-anything-albert',
    version='1.0.0',
    packages=['cli_anything.albert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-albert=cli_anything.albert:cli']},
)
