from setuptools import setup
setup(
    name='cli-anything-ajv',
    version='1.0.0',
    packages=['cli_anything.ajv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ajv=cli_anything.ajv:cli']},
)
