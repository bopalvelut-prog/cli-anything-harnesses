from setuptools import setup
setup(
    name='cli-anything-amazon_sso',
    version='1.0.0',
    packages=['cli_anything.amazon_sso'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_sso=cli_anything.amazon_sso:cli']},
)
