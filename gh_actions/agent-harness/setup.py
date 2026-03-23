from setuptools import setup
setup(
    name='cli-anything-gh_actions',
    version='1.0.0',
    packages=['cli_anything.gh_actions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gh_actions=cli_anything.gh_actions:cli']},
)
