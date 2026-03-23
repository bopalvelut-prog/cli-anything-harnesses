from setuptools import setup
setup(
    name='cli-anything-remotion',
    version='1.0.0',
    packages=['cli_anything.remotion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remotion=cli_anything.remotion:cli']},
)
