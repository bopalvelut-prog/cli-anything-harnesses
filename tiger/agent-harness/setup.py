from setuptools import setup
setup(
    name='cli-anything-tiger',
    version='1.0.0',
    packages=['cli_anything.tiger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tiger=cli_anything.tiger:cli']},
)
