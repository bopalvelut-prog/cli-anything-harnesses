from setuptools import setup
setup(
    name='cli-anything-bunny',
    version='1.0.0',
    packages=['cli_anything.bunny'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bunny=cli_anything.bunny:cli']},
)
