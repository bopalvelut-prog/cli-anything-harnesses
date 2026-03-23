from setuptools import setup
setup(
    name='cli-anything-amazon_kendra',
    version='1.0.0',
    packages=['cli_anything.amazon_kendra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_kendra=cli_anything.amazon_kendra:cli']},
)
