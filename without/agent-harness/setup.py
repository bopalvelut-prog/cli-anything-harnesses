from setuptools import setup
setup(
    name='cli-anything-without',
    version='1.0.0',
    packages=['cli_anything.without'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-without=cli_anything.without:cli']},
)
