from setuptools import setup
setup(
    name='cli-anything-object',
    version='1.0.0',
    packages=['cli_anything.object'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-object=cli_anything.object:cli']},
)
