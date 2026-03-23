from setuptools import setup
setup(
    name='cli-anything-deployer',
    version='1.0.0',
    packages=['cli_anything.deployer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deployer=cli_anything.deployer:cli']},
)
