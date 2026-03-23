from setuptools import setup
setup(
    name='cli-anything-tag',
    version='1.0.0',
    packages=['cli_anything.tag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tag=cli_anything.tag:cli']},
)
