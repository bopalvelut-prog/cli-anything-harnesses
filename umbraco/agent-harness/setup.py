from setuptools import setup
setup(
    name='cli-anything-umbraco',
    version='1.0.0',
    packages=['cli_anything.umbraco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-umbraco=cli_anything.umbraco:cli']},
)
