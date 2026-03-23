from setuptools import setup
setup(
    name='cli-anything-target',
    version='1.0.0',
    packages=['cli_anything.target'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-target=cli_anything.target:cli']},
)
