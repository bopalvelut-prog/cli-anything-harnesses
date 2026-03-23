from setuptools import setup
setup(
    name='cli-anything-amazon_emr',
    version='1.0.0',
    packages=['cli_anything.amazon_emr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_emr=cli_anything.amazon_emr:cli']},
)
