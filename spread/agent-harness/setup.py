from setuptools import setup
setup(
    name='cli-anything-spread',
    version='1.0.0',
    packages=['cli_anything.spread'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spread=cli_anything.spread:cli']},
)
