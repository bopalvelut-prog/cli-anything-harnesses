from setuptools import setup
setup(
    name='cli-anything-echo',
    version='1.0.0',
    packages=['cli_anything.echo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-echo=cli_anything.echo:cli']},
)
