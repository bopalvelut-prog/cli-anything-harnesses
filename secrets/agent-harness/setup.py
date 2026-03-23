from setuptools import setup
setup(
    name='cli-anything-secrets',
    version='1.0.0',
    packages=['cli_anything.secrets'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-secrets=cli_anything.secrets:cli']},
)
