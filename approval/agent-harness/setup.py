from setuptools import setup
setup(
    name='cli-anything-approval',
    version='1.0.0',
    packages=['cli_anything.approval'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-approval=cli_anything.approval:cli']},
)
