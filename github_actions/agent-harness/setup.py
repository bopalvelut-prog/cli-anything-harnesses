from setuptools import setup
setup(
    name='cli-anything-github_actions',
    version='1.0.0',
    packages=['cli_anything.github_actions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-github_actions=cli_anything.github_actions:cli']},
)
