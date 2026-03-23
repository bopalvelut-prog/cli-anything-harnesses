from setuptools import setup
setup(
    name='cli-anything-edit',
    version='1.0.0',
    packages=['cli_anything.edit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-edit=cli_anything.edit:cli']},
)
