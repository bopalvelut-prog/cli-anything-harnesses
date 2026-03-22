from setuptools import setup
setup(
    name='cli-anything-wufoo',
    version='1.0.0',
    packages=['cli_anything.wufoo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wufoo=cli_anything.wufoo:cli']},
)
