from setuptools import setup
setup(
    name='cli-anything-codefresh',
    version='1.0.0',
    packages=['cli_anything.codefresh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codefresh=cli_anything.codefresh:cli']},
)
