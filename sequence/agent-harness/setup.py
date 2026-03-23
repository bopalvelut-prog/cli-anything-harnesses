from setuptools import setup
setup(
    name='cli-anything-sequence',
    version='1.0.0',
    packages=['cli_anything.sequence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sequence=cli_anything.sequence:cli']},
)
