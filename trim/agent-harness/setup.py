from setuptools import setup
setup(
    name='cli-anything-trim',
    version='1.0.0',
    packages=['cli_anything.trim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trim=cli_anything.trim:cli']},
)
