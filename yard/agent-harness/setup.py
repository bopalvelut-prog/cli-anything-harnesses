from setuptools import setup
setup(
    name='cli-anything-yard',
    version='1.0.0',
    packages=['cli_anything.yard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yard=cli_anything.yard:cli']},
)
