from setuptools import setup
setup(
    name='cli-anything-quarkus',
    version='1.0.0',
    packages=['cli_anything.quarkus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quarkus=cli_anything.quarkus:cli']},
)
