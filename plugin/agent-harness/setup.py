from setuptools import setup
setup(
    name='cli-anything-plugin',
    version='1.0.0',
    packages=['cli_anything.plugin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plugin=cli_anything.plugin:cli']},
)
