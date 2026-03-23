from setuptools import setup
setup(
    name='cli-anything-science',
    version='1.0.0',
    packages=['cli_anything.science'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-science=cli_anything.science:cli']},
)
