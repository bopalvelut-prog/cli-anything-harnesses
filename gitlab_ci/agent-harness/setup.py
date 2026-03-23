from setuptools import setup
setup(
    name='cli-anything-gitlab_ci',
    version='1.0.0',
    packages=['cli_anything.gitlab_ci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitlab_ci=cli_anything.gitlab_ci:cli']},
)
