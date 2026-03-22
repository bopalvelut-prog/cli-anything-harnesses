from setuptools import setup
setup(
    name='cli-anything-moonbeam',
    version='1.0.0',
    packages=['cli_anything.moonbeam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moonbeam=cli_anything.moonbeam:cli']},
)
