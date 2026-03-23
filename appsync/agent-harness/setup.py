from setuptools import setup
setup(
    name='cli-anything-appsync',
    version='1.0.0',
    packages=['cli_anything.appsync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appsync=cli_anything.appsync:cli']},
)
