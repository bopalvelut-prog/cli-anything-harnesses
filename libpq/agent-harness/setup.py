from setuptools import setup
setup(
    name='cli-anything-libpq',
    version='1.0.0',
    packages=['cli_anything.libpq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libpq=cli_anything.libpq:cli']},
)
