from setuptools import setup
setup(
    name='cli-anything-content',
    version='1.0.0',
    packages=['cli_anything.content'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-content=cli_anything.content:cli']},
)
