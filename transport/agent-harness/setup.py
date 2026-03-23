from setuptools import setup
setup(
    name='cli-anything-transport',
    version='1.0.0',
    packages=['cli_anything.transport'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transport=cli_anything.transport:cli']},
)
