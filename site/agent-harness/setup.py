from setuptools import setup
setup(
    name='cli-anything-site',
    version='1.0.0',
    packages=['cli_anything.site'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-site=cli_anything.site:cli']},
)
