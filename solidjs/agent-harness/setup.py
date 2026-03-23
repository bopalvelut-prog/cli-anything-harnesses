from setuptools import setup
setup(
    name='cli-anything-solidjs',
    version='1.0.0',
    packages=['cli_anything.solidjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-solidjs=cli_anything.solidjs:cli']},
)
