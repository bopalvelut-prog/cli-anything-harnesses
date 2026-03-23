from setuptools import setup
setup(
    name='cli-anything-confirm',
    version='1.0.0',
    packages=['cli_anything.confirm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-confirm=cli_anything.confirm:cli']},
)
