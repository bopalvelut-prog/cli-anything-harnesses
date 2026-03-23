from setuptools import setup
setup(
    name='cli-anything-void',
    version='1.0.0',
    packages=['cli_anything.void'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-void=cli_anything.void:cli']},
)
