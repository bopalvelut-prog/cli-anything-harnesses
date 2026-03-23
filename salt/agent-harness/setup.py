from setuptools import setup
setup(
    name='cli-anything-salt',
    version='1.0.0',
    packages=['cli_anything.salt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-salt=cli_anything.salt:cli']},
)
