from setuptools import setup
setup(
    name='cli-anything-reform',
    version='1.0.0',
    packages=['cli_anything.reform'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reform=cli_anything.reform:cli']},
)
