from setuptools import setup
setup(
    name='cli-anything-semgrep',
    version='1.0.0',
    packages=['cli_anything.semgrep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-semgrep=cli_anything.semgrep:cli']},
)
