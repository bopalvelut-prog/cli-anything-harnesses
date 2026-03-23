from setuptools import setup
setup(
    name='cli-anything-sandstorm',
    version='1.0.0',
    packages=['cli_anything.sandstorm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sandstorm=cli_anything.sandstorm:cli']},
)
