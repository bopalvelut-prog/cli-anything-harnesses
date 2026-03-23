from setuptools import setup
setup(
    name='cli-anything-static_site',
    version='1.0.0',
    packages=['cli_anything.static_site'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-static_site=cli_anything.static_site:cli']},
)
