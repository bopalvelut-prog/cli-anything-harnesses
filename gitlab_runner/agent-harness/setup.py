from setuptools import setup
setup(
    name='cli-anything-gitlab_runner',
    version='1.0.0',
    packages=['cli_anything.gitlab_runner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitlab_runner=cli_anything.gitlab_runner:cli']},
)
