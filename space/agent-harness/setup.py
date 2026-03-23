from setuptools import setup
setup(
    name='cli-anything-space',
    version='1.0.0',
    packages=['cli_anything.space'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-space=cli_anything.space:cli']},
)
