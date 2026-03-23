from setuptools import setup
setup(
    name='cli-anything-github_pages',
    version='1.0.0',
    packages=['cli_anything.github_pages'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-github_pages=cli_anything.github_pages:cli']},
)
