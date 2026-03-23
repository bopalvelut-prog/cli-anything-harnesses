from setuptools import setup
setup(
    name='cli-anything-application_insights',
    version='1.0.0',
    packages=['cli_anything.application_insights'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-application_insights=cli_anything.application_insights:cli']},
)
