from setuptools import setup
setup(
    name='cli-anything-website',
    version='1.0.0',
    packages=['cli_anything.website'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-website=cli_anything.website:cli']},
)
