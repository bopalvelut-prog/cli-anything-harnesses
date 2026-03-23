from setuptools import setup
setup(
    name='cli-anything-ordinary',
    version='1.0.0',
    packages=['cli_anything.ordinary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ordinary=cli_anything.ordinary:cli']},
)
