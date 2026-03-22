from setuptools import setup
setup(
    name='cli-anything-sendgrid',
    version='1.0.0',
    packages=['cli_anything.sendgrid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sendgrid=cli_anything.sendgrid:cli']},
)
