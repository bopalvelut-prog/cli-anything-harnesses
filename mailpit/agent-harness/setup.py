from setuptools import setup
setup(
    name='cli-anything-mailpit',
    version='1.0.0',
    packages=['cli_anything.mailpit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailpit=cli_anything.mailpit:cli']},
)
