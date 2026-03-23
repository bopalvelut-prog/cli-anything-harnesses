from setuptools import setup
setup(
    name='cli-anything-jwt',
    version='1.0.0',
    packages=['cli_anything.jwt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jwt=cli_anything.jwt:cli']},
)
