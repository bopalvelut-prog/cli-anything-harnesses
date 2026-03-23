from setuptools import setup
setup(
    name='cli-anything-aspire',
    version='1.0.0',
    packages=['cli_anything.aspire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aspire=cli_anything.aspire:cli']},
)
