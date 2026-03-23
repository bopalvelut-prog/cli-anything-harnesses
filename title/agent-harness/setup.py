from setuptools import setup
setup(
    name='cli-anything-title',
    version='1.0.0',
    packages=['cli_anything.title'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-title=cli_anything.title:cli']},
)
