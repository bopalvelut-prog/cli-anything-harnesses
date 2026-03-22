from setuptools import setup
setup(
    name='cli-anything-pandoc_mkdocs',
    version='1.0.0',
    packages=['cli_anything.pandoc_mkdocs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pandoc_mkdocs=cli_anything.pandoc_mkdocs:cli']},
)
