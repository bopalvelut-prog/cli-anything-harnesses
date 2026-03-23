from setuptools import setup
setup(
    name='cli-anything-backstage',
    version='1.0.0',
    packages=['cli_anything.backstage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-backstage=cli_anything.backstage:cli']},
)
