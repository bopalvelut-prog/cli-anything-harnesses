from setuptools import setup
setup(
    name='cli-anything-steep',
    version='1.0.0',
    packages=['cli_anything.steep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-steep=cli_anything.steep:cli']},
)
