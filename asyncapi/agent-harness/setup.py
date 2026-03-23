from setuptools import setup
setup(
    name='cli-anything-asyncapi',
    version='1.0.0',
    packages=['cli_anything.asyncapi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asyncapi=cli_anything.asyncapi:cli']},
)
