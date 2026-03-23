from setuptools import setup
setup(
    name='cli-anything-provider',
    version='1.0.0',
    packages=['cli_anything.provider'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-provider=cli_anything.provider:cli']},
)
