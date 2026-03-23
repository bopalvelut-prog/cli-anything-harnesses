from setuptools import setup
setup(
    name='cli-anything-xslt',
    version='1.0.0',
    packages=['cli_anything.xslt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xslt=cli_anything.xslt:cli']},
)
