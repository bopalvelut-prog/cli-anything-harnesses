from setuptools import setup
setup(
    name='cli-anything-terragrunt',
    version='1.0.0',
    packages=['cli_anything.terragrunt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terragrunt=cli_anything.terragrunt:cli']},
)
