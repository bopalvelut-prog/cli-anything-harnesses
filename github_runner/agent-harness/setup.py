from setuptools import setup
setup(
    name='cli-anything-github_runner',
    version='1.0.0',
    packages=['cli_anything.github_runner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-github_runner=cli_anything.github_runner:cli']},
)
