from setuptools import setup
setup(
    name='cli-anything-null',
    version='1.0.0',
    packages=['cli_anything.null'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-null=cli_anything.null:cli']},
)
