from setuptools import setup
setup(
    name='cli-anything-focus',
    version='1.0.0',
    packages=['cli_anything.focus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-focus=cli_anything.focus:cli']},
)
