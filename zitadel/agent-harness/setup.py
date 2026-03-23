from setuptools import setup
setup(
    name='cli-anything-zitadel',
    version='1.0.0',
    packages=['cli_anything.zitadel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zitadel=cli_anything.zitadel:cli']},
)
