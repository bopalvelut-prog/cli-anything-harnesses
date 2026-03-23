from setuptools import setup
setup(
    name='cli-anything-authorize',
    version='1.0.0',
    packages=['cli_anything.authorize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-authorize=cli_anything.authorize:cli']},
)
