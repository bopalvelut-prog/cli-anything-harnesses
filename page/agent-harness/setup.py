from setuptools import setup
setup(
    name='cli-anything-page',
    version='1.0.0',
    packages=['cli_anything.page'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-page=cli_anything.page:cli']},
)
