from setuptools import setup
setup(
    name='cli-anything-scroll',
    version='1.0.0',
    packages=['cli_anything.scroll'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scroll=cli_anything.scroll:cli']},
)
