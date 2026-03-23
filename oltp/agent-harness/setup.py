from setuptools import setup
setup(
    name='cli-anything-oltp',
    version='1.0.0',
    packages=['cli_anything.oltp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oltp=cli_anything.oltp:cli']},
)
