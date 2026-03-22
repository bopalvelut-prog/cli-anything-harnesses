from setuptools import setup
setup(
    name='cli-anything-sitecore',
    version='1.0.0',
    packages=['cli_anything.sitecore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sitecore=cli_anything.sitecore:cli']},
)
