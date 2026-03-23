from setuptools import setup
setup(
    name='cli-anything-auth',
    version='1.0.0',
    packages=['cli_anything.auth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-auth=cli_anything.auth:cli']},
)
