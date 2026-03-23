from setuptools import setup
setup(
    name='cli-anything-vivid',
    version='1.0.0',
    packages=['cli_anything.vivid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vivid=cli_anything.vivid:cli']},
)
