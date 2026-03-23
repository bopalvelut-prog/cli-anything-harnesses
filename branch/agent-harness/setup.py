from setuptools import setup
setup(
    name='cli-anything-branch',
    version='1.0.0',
    packages=['cli_anything.branch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-branch=cli_anything.branch:cli']},
)
