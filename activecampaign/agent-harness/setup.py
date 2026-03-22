from setuptools import setup
setup(
    name='cli-anything-activecampaign',
    version='1.0.0',
    packages=['cli_anything.activecampaign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-activecampaign=cli_anything.activecampaign:cli']},
)
