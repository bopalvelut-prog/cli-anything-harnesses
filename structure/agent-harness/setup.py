from setuptools import setup
setup(
    name='cli-anything-structure',
    version='1.0.0',
    packages=['cli_anything.structure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-structure=cli_anything.structure:cli']},
)
