from setuptools import setup
setup(
    name='cli-anything-rest_api',
    version='1.0.0',
    packages=['cli_anything.rest_api'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rest_api=cli_anything.rest_api:cli']},
)
