from setuptools import setup
setup(
    name='cli-anything-thanks',
    version='1.0.0',
    packages=['cli_anything.thanks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thanks=cli_anything.thanks:cli']},
)
