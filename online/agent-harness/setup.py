from setuptools import setup
setup(
    name='cli-anything-online',
    version='1.0.0',
    packages=['cli_anything.online'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-online=cli_anything.online:cli']},
)
