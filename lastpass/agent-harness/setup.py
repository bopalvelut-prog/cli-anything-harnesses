from setuptools import setup
setup(
    name='cli-anything-lastpass',
    version='1.0.0',
    packages=['cli_anything.lastpass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lastpass=cli_anything.lastpass:cli']},
)
