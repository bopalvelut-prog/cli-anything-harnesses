from setuptools import setup
setup(
    name='cli-anything-through',
    version='1.0.0',
    packages=['cli_anything.through'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-through=cli_anything.through:cli']},
)
