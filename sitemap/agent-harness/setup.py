from setuptools import setup
setup(
    name='cli-anything-sitemap',
    version='1.0.0',
    packages=['cli_anything.sitemap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sitemap=cli_anything.sitemap:cli']},
)
