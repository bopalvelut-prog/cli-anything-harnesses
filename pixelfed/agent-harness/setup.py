from setuptools import setup
setup(
    name='cli-anything-pixelfed',
    version='1.0.0',
    packages=['cli_anything.pixelfed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pixelfed=cli_anything.pixelfed:cli']},
)
