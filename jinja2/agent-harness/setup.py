from setuptools import setup
setup(
    name='cli-anything-jinja2',
    version='1.0.0',
    packages=['cli_anything.jinja2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jinja2=cli_anything.jinja2:cli']},
)
