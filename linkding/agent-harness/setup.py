from setuptools import setup
setup(
    name='cli-anything-linkding',
    version='1.0.0',
    packages=['cli_anything.linkding'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linkding=cli_anything.linkding:cli']},
)
