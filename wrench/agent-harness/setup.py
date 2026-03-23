from setuptools import setup
setup(
    name='cli-anything-wrench',
    version='1.0.0',
    packages=['cli_anything.wrench'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wrench=cli_anything.wrench:cli']},
)
