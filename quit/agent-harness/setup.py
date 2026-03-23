from setuptools import setup
setup(
    name='cli-anything-quit',
    version='1.0.0',
    packages=['cli_anything.quit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quit=cli_anything.quit:cli']},
)
