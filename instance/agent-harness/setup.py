from setuptools import setup
setup(
    name='cli-anything-instance',
    version='1.0.0',
    packages=['cli_anything.instance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-instance=cli_anything.instance:cli']},
)
