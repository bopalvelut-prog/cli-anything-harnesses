from setuptools import setup
setup(
    name='cli-anything-active',
    version='1.0.0',
    packages=['cli_anything.active'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-active=cli_anything.active:cli']},
)
