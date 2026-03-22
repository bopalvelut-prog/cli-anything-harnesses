from setuptools import setup
setup(
    name='cli-anything-terraform_cloud',
    version='1.0.0',
    packages=['cli_anything.terraform_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terraform_cloud=cli_anything.terraform_cloud:cli']},
)
