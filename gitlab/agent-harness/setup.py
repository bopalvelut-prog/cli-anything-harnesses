from setuptools import setup
setup(
    name='cli-anything-gitlab',
    version='1.0.0',
    packages=['cli_anything.gitlab'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-gitlab=cli_anything.gitlab:cli']},
)
