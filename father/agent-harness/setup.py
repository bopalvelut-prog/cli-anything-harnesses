from setuptools import setup
setup(
    name='cli-anything-father',
    version='1.0.0',
    packages=['cli_anything.father'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-father=cli_anything.father:cli']},
)
