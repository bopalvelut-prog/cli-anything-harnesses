from setuptools import setup
setup(
    name='cli-anything-place',
    version='1.0.0',
    packages=['cli_anything.place'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-place=cli_anything.place:cli']},
)
