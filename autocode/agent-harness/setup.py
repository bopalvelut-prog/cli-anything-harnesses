from setuptools import setup
setup(
    name='cli-anything-autocode',
    version='1.0.0',
    packages=['cli_anything.autocode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autocode=cli_anything.autocode:cli']},
)
