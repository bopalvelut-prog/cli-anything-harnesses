from setuptools import setup
setup(
    name='cli-anything-coder',
    version='1.0.0',
    packages=['cli_anything.coder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coder=cli_anything.coder:cli']},
)
