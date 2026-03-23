from setuptools import setup
setup(
    name='cli-anything-pool',
    version='1.0.0',
    packages=['cli_anything.pool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pool=cli_anything.pool:cli']},
)
