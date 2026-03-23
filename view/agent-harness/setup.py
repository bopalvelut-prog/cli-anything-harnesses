from setuptools import setup
setup(
    name='cli-anything-view',
    version='1.0.0',
    packages=['cli_anything.view'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-view=cli_anything.view:cli']},
)
