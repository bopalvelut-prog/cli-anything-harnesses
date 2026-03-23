from setuptools import setup
setup(
    name='cli-anything-friend',
    version='1.0.0',
    packages=['cli_anything.friend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-friend=cli_anything.friend:cli']},
)
