from setuptools import setup
setup(
    name='cli-anything-amazon_codeguru',
    version='1.0.0',
    packages=['cli_anything.amazon_codeguru'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_codeguru=cli_anything.amazon_codeguru:cli']},
)
