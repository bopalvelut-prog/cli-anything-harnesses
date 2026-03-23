from setuptools import setup
setup(
    name='cli-anything-trouble',
    version='1.0.0',
    packages=['cli_anything.trouble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trouble=cli_anything.trouble:cli']},
)
