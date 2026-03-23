from setuptools import setup
setup(
    name='cli-anything-field',
    version='1.0.0',
    packages=['cli_anything.field'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-field=cli_anything.field:cli']},
)
