from setuptools import setup
setup(
    name='cli-anything-industry',
    version='1.0.0',
    packages=['cli_anything.industry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-industry=cli_anything.industry:cli']},
)
