from setuptools import setup
setup(
    name='cli-anything-github_enterprise',
    version='1.0.0',
    packages=['cli_anything.github_enterprise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-github_enterprise=cli_anything.github_enterprise:cli']},
)
