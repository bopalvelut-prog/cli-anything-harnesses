from setuptools import setup
setup(
    name='cli-anything-fish',
    version='1.0.0',
    packages=['cli_anything.fish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fish=cli_anything.fish:cli']},
)
