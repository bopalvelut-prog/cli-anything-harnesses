from setuptools import setup
setup(
    name='cli-anything-rye',
    version='1.0.0',
    packages=['cli_anything.rye'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rye=cli_anything.rye:cli']},
)
