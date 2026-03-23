from setuptools import setup
setup(
    name='cli-anything-thorn',
    version='1.0.0',
    packages=['cli_anything.thorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thorn=cli_anything.thorn:cli']},
)
