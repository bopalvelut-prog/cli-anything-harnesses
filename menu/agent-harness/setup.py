from setuptools import setup
setup(
    name='cli-anything-menu',
    version='1.0.0',
    packages=['cli_anything.menu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-menu=cli_anything.menu:cli']},
)
