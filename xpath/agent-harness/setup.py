from setuptools import setup
setup(
    name='cli-anything-xpath',
    version='1.0.0',
    packages=['cli_anything.xpath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xpath=cli_anything.xpath:cli']},
)
