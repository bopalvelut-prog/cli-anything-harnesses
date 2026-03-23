from setuptools import setup
setup(
    name='cli-anything-tabby',
    version='1.0.0',
    packages=['cli_anything.tabby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tabby=cli_anything.tabby:cli']},
)
