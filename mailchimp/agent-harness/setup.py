from setuptools import setup
setup(
    name='cli-anything-mailchimp',
    version='1.0.0',
    packages=['cli_anything.mailchimp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailchimp=cli_anything.mailchimp:cli']},
)
