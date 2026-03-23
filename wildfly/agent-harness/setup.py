from setuptools import setup
setup(
    name='cli-anything-wildfly',
    version='1.0.0',
    packages=['cli_anything.wildfly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wildfly=cli_anything.wildfly:cli']},
)
