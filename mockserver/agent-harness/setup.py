from setuptools import setup
setup(
    name='cli-anything-mockserver',
    version='1.0.0',
    packages=['cli_anything.mockserver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mockserver=cli_anything.mockserver:cli']},
)
