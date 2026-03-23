from setuptools import setup
setup(
    name='cli-anything-bee',
    version='1.0.0',
    packages=['cli_anything.bee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bee=cli_anything.bee:cli']},
)
