from setuptools import setup
setup(
    name='cli-anything-setup',
    version='1.0.0',
    packages=['cli_anything.setup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-setup=cli_anything.setup:cli']},
)
