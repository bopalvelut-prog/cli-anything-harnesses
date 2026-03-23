from setuptools import setup
setup(
    name='cli-anything-w',
    version='1.0.0',
    packages=['cli_anything.w'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-w=cli_anything.w:cli']},
)
