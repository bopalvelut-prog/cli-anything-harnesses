from setuptools import setup
setup(
    name='cli-anything-amazon_workdocs',
    version='1.0.0',
    packages=['cli_anything.amazon_workdocs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_workdocs=cli_anything.amazon_workdocs:cli']},
)
