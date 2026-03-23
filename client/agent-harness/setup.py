from setuptools import setup
setup(
    name='cli-anything-client',
    version='1.0.0',
    packages=['cli_anything.client'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-client=cli_anything.client:cli']},
)
