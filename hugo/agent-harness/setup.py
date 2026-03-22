from setuptools import setup
setup(
    name='cli-anything-hugo',
    version='1.0.0',
    packages=['cli_anything.hugo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hugo=cli_anything.hugo:cli']},
)
