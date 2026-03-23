from setuptools import setup
setup(
    name='cli-anything-claude',
    version='1.0.0',
    packages=['cli_anything.claude'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-claude=cli_anything.claude:cli']},
)
