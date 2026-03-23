from setuptools import setup
setup(
    name='cli-anything-shoot',
    version='1.0.0',
    packages=['cli_anything.shoot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shoot=cli_anything.shoot:cli']},
)
