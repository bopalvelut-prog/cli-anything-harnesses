from setuptools import setup
setup(
    name='cli-anything-amazon_workmail',
    version='1.0.0',
    packages=['cli_anything.amazon_workmail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_workmail=cli_anything.amazon_workmail:cli']},
)
