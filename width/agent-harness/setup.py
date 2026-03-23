from setuptools import setup
setup(
    name='cli-anything-width',
    version='1.0.0',
    packages=['cli_anything.width'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-width=cli_anything.width:cli']},
)
