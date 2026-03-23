from setuptools import setup
setup(
    name='cli-anything-ssl',
    version='1.0.0',
    packages=['cli_anything.ssl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ssl=cli_anything.ssl:cli']},
)
