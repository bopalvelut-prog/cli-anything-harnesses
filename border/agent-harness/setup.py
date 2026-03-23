from setuptools import setup
setup(
    name='cli-anything-border',
    version='1.0.0',
    packages=['cli_anything.border'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-border=cli_anything.border:cli']},
)
