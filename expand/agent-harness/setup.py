from setuptools import setup
setup(
    name='cli-anything-expand',
    version='1.0.0',
    packages=['cli_anything.expand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-expand=cli_anything.expand:cli']},
)
