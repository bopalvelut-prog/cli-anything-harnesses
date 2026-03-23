from setuptools import setup
setup(
    name='cli-anything-plone',
    version='1.0.0',
    packages=['cli_anything.plone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plone=cli_anything.plone:cli']},
)
