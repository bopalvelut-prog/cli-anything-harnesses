from setuptools import setup
setup(
    name='cli-anything-improve',
    version='1.0.0',
    packages=['cli_anything.improve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-improve=cli_anything.improve:cli']},
)
