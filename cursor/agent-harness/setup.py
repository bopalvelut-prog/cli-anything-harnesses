from setuptools import setup
setup(
    name='cli-anything-cursor',
    version='1.0.0',
    packages=['cli_anything.cursor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cursor=cli_anything.cursor:cli']},
)
