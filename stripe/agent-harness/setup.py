from setuptools import setup
setup(
    name='cli-anything-stripe',
    version='1.0.0',
    packages=['cli_anything.stripe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stripe=cli_anything.stripe:cli']},
)
