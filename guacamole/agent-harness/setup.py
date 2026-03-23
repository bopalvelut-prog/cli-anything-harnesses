from setuptools import setup
setup(
    name='cli-anything-guacamole',
    version='1.0.0',
    packages=['cli_anything.guacamole'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guacamole=cli_anything.guacamole:cli']},
)
