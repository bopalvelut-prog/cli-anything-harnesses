from setuptools import setup
setup(
    name='cli-anything-apollo',
    version='1.0.0',
    packages=['cli_anything.apollo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apollo=cli_anything.apollo:cli']},
)
