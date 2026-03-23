from setuptools import setup
setup(
    name='cli-anything-pre',
    version='1.0.0',
    packages=['cli_anything.pre'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pre=cli_anything.pre:cli']},
)
