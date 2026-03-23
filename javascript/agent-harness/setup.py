from setuptools import setup
setup(
    name='cli-anything-javascript',
    version='1.0.0',
    packages=['cli_anything.javascript'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-javascript=cli_anything.javascript:cli']},
)
