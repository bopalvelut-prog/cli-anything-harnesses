from setuptools import setup
setup(
    name='cli-anything-link',
    version='1.0.0',
    packages=['cli_anything.link'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-link=cli_anything.link:cli']},
)
