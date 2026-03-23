from setuptools import setup
setup(
    name='cli-anything-tenant',
    version='1.0.0',
    packages=['cli_anything.tenant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tenant=cli_anything.tenant:cli']},
)
