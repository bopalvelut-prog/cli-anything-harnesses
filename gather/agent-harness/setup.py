from setuptools import setup
setup(
    name='cli-anything-gather',
    version='1.0.0',
    packages=['cli_anything.gather'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gather=cli_anything.gather:cli']},
)
