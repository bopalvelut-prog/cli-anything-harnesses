from setuptools import setup
setup(
    name='cli-anything-nushell',
    version='1.0.0',
    packages=['cli_anything.nushell'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nushell=cli_anything.nushell:cli']},
)
