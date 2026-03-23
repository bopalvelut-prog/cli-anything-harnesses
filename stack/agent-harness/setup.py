from setuptools import setup
setup(
    name='cli-anything-stack',
    version='1.0.0',
    packages=['cli_anything.stack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stack=cli_anything.stack:cli']},
)
