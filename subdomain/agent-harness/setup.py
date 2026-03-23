from setuptools import setup
setup(
    name='cli-anything-subdomain',
    version='1.0.0',
    packages=['cli_anything.subdomain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subdomain=cli_anything.subdomain:cli']},
)
