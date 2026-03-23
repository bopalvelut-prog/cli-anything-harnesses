from setuptools import setup
setup(
    name='cli-anything-ranger',
    version='1.0.0',
    packages=['cli_anything.ranger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ranger=cli_anything.ranger:cli']},
)
