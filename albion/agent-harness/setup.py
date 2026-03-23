from setuptools import setup
setup(
    name='cli-anything-albion',
    version='1.0.0',
    packages=['cli_anything.albion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-albion=cli_anything.albion:cli']},
)
