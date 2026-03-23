from setuptools import setup
setup(
    name='cli-anything-novel',
    version='1.0.0',
    packages=['cli_anything.novel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-novel=cli_anything.novel:cli']},
)
