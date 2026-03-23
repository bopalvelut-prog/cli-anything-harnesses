from setuptools import setup
setup(
    name='cli-anything-hurl',
    version='1.0.0',
    packages=['cli_anything.hurl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hurl=cli_anything.hurl:cli']},
)
