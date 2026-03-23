from setuptools import setup
setup(
    name='cli-anything-action',
    version='1.0.0',
    packages=['cli_anything.action'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-action=cli_anything.action:cli']},
)
