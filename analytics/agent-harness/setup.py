from setuptools import setup
setup(
    name='cli-anything-analytics',
    version='1.0.0',
    packages=['cli_anything.analytics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-analytics=cli_anything.analytics:cli']},
)
