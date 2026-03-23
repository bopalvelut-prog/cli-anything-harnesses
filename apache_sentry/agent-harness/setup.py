from setuptools import setup
setup(
    name='cli-anything-apache_sentry',
    version='1.0.0',
    packages=['cli_anything.apache_sentry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_sentry=cli_anything.apache_sentry:cli']},
)
