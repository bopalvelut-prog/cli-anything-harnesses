from setuptools import setup
setup(
    name='cli-anything-save',
    version='1.0.0',
    packages=['cli_anything.save'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-save=cli_anything.save:cli']},
)
