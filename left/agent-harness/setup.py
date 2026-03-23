from setuptools import setup
setup(
    name='cli-anything-left',
    version='1.0.0',
    packages=['cli_anything.left'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-left=cli_anything.left:cli']},
)
