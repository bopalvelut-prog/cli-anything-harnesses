from setuptools import setup
setup(
    name='cli-anything-lime',
    version='1.0.0',
    packages=['cli_anything.lime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lime=cli_anything.lime:cli']},
)
