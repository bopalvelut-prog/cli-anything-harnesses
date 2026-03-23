from setuptools import setup
setup(
    name='cli-anything-kairosdb',
    version='1.0.0',
    packages=['cli_anything.kairosdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kairosdb=cli_anything.kairosdb:cli']},
)
