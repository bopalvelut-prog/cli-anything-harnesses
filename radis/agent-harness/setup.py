from setuptools import setup
setup(
    name='cli-anything-radis',
    version='1.0.0',
    packages=['cli_anything.radis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radis=cli_anything.radis:cli']},
)
