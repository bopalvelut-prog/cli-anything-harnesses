from setuptools import setup
setup(
    name='cli-anything-guest',
    version='1.0.0',
    packages=['cli_anything.guest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guest=cli_anything.guest:cli']},
)
