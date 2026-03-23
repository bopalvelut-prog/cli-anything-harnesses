from setuptools import setup
setup(
    name='cli-anything-update',
    version='1.0.0',
    packages=['cli_anything.update'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-update=cli_anything.update:cli']},
)
