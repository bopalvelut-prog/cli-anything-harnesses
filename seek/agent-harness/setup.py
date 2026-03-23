from setuptools import setup
setup(
    name='cli-anything-seek',
    version='1.0.0',
    packages=['cli_anything.seek'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seek=cli_anything.seek:cli']},
)
