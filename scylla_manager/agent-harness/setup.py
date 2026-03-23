from setuptools import setup
setup(
    name='cli-anything-scylla_manager',
    version='1.0.0',
    packages=['cli_anything.scylla_manager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scylla_manager=cli_anything.scylla_manager:cli']},
)
