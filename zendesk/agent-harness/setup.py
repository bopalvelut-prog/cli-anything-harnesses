from setuptools import setup
setup(
    name='cli-anything-zendesk',
    version='1.0.0',
    packages=['cli_anything.zendesk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zendesk=cli_anything.zendesk:cli']},
)
