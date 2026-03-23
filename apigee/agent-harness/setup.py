from setuptools import setup
setup(
    name='cli-anything-apigee',
    version='1.0.0',
    packages=['cli_anything.apigee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apigee=cli_anything.apigee:cli']},
)
