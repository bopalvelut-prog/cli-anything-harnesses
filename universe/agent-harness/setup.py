from setuptools import setup
setup(
    name='cli-anything-universe',
    version='1.0.0',
    packages=['cli_anything.universe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-universe=cli_anything.universe:cli']},
)
