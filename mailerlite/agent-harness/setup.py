from setuptools import setup
setup(
    name='cli-anything-mailerlite',
    version='1.0.0',
    packages=['cli_anything.mailerlite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailerlite=cli_anything.mailerlite:cli']},
)
