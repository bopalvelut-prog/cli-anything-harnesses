from setuptools import setup
setup(
    name='cli-anything-vault',
    version='1.0.0',
    packages=['cli_anything.vault'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vault=cli_anything.vault:cli']},
)
