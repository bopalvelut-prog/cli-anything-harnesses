from setuptools import setup
setup(
    name='cli-anything-fiction',
    version='1.0.0',
    packages=['cli_anything.fiction'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fiction=cli_anything.fiction:cli']},
)
