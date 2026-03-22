from setuptools import setup
setup(
    name='cli-anything-tfsec',
    version='1.0.0',
    packages=['cli_anything.tfsec'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tfsec=cli_anything.tfsec:cli']},
)
