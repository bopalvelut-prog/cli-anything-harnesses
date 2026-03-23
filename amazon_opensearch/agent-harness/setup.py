from setuptools import setup
setup(
    name='cli-anything-amazon_opensearch',
    version='1.0.0',
    packages=['cli_anything.amazon_opensearch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_opensearch=cli_anything.amazon_opensearch:cli']},
)
