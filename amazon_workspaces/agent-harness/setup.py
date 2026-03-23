from setuptools import setup
setup(
    name='cli-anything-amazon_workspaces',
    version='1.0.0',
    packages=['cli_anything.amazon_workspaces'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_workspaces=cli_anything.amazon_workspaces:cli']},
)
