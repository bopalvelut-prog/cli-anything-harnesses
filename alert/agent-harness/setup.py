from setuptools import setup
setup(
    name='cli-anything-alert',
    version='1.0.0',
    packages=['cli_anything.alert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alert=cli_anything.alert:cli']},
)
