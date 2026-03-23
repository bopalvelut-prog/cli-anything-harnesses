from setuptools import setup
setup(
    name='cli-anything-third',
    version='1.0.0',
    packages=['cli_anything.third'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-third=cli_anything.third:cli']},
)
