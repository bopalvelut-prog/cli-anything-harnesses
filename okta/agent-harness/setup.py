from setuptools import setup
setup(
    name='cli-anything-okta',
    version='1.0.0',
    packages=['cli_anything.okta'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-okta=cli_anything.okta:cli']},
)
