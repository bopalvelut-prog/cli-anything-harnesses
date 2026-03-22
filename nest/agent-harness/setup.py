from setuptools import setup
setup(
    name='cli-anything-nest',
    version='1.0.0',
    packages=['cli_anything.nest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nest=cli_anything.nest:cli']},
)
