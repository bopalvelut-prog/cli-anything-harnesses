from setuptools import setup
setup(
    name='cli-anything-maven_plugin',
    version='1.0.0',
    packages=['cli_anything.maven_plugin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maven_plugin=cli_anything.maven_plugin:cli']},
)
