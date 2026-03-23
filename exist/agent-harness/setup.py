from setuptools import setup
setup(
    name='cli-anything-exist',
    version='1.0.0',
    packages=['cli_anything.exist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exist=cli_anything.exist:cli']},
)
