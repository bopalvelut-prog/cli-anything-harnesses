from setuptools import setup
setup(
    name='cli-anything-sharding',
    version='1.0.0',
    packages=['cli_anything.sharding'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sharding=cli_anything.sharding:cli']},
)
