from setuptools import setup
setup(
    name='cli-anything-formbricks',
    version='1.0.0',
    packages=['cli_anything.formbricks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formbricks=cli_anything.formbricks:cli']},
)
