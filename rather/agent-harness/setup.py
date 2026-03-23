from setuptools import setup
setup(
    name='cli-anything-rather',
    version='1.0.0',
    packages=['cli_anything.rather'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rather=cli_anything.rather:cli']},
)
