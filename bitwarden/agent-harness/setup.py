from setuptools import setup
setup(
    name='cli-anything-bitwarden',
    version='1.0.0',
    packages=['cli_anything.bitwarden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitwarden=cli_anything.bitwarden:cli']},
)
