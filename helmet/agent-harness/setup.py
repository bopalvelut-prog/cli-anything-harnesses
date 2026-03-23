from setuptools import setup
setup(
    name='cli-anything-helmet',
    version='1.0.0',
    packages=['cli_anything.helmet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-helmet=cli_anything.helmet:cli']},
)
