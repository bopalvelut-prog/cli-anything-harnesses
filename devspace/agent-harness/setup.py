from setuptools import setup
setup(
    name='cli-anything-devspace',
    version='1.0.0',
    packages=['cli_anything.devspace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devspace=cli_anything.devspace:cli']},
)
