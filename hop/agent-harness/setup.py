from setuptools import setup
setup(
    name='cli-anything-hop',
    version='1.0.0',
    packages=['cli_anything.hop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hop=cli_anything.hop:cli']},
)
