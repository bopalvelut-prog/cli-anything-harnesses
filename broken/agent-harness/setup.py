from setuptools import setup
setup(
    name='cli-anything-broken',
    version='1.0.0',
    packages=['cli_anything.broken'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-broken=cli_anything.broken:cli']},
)
