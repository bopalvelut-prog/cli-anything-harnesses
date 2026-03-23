from setuptools import setup
setup(
    name='cli-anything-diamond',
    version='1.0.0',
    packages=['cli_anything.diamond'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-diamond=cli_anything.diamond:cli']},
)
