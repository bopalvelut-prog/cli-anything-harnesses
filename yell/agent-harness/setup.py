from setuptools import setup
setup(
    name='cli-anything-yell',
    version='1.0.0',
    packages=['cli_anything.yell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yell=cli_anything.yell:cli']},
)
