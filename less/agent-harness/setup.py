from setuptools import setup
setup(
    name='cli-anything-less',
    version='1.0.0',
    packages=['cli_anything.less'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-less=cli_anything.less:cli']},
)
