from setuptools import setup
setup(
    name='cli-anything-squid',
    version='1.0.0',
    packages=['cli_anything.squid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-squid=cli_anything.squid:cli']},
)
