from setuptools import setup
setup(
    name='cli-anything-apache_lens',
    version='1.0.0',
    packages=['cli_anything.apache_lens'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apache_lens=cli_anything.apache_lens:cli']},
)
