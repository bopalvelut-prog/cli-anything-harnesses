from setuptools import setup
setup(
    name='cli-anything-unmark',
    version='1.0.0',
    packages=['cli_anything.unmark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unmark=cli_anything.unmark:cli']},
)
