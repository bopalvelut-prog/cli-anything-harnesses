from setuptools import setup
setup(
    name='cli-anything-mailgun',
    version='1.0.0',
    packages=['cli_anything.mailgun'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailgun=cli_anything.mailgun:cli']},
)
