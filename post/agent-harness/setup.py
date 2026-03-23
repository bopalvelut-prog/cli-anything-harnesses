from setuptools import setup
setup(
    name='cli-anything-post',
    version='1.0.0',
    packages=['cli_anything.post'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-post=cli_anything.post:cli']},
)
