from setuptools import setup
setup(
    name='cli-anything-hashicorp',
    version='1.0.0',
    packages=['cli_anything.hashicorp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hashicorp=cli_anything.hashicorp:cli']},
)
