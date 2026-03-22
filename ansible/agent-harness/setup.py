from setuptools import setup
setup(
    name='cli-anything-ansible',
    version='1.0.0',
    packages=['cli_anything.ansible'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ansible=cli_anything.ansible:cli']},
)
