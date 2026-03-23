from setuptools import setup
setup(
    name='cli-anything-paste',
    version='1.0.0',
    packages=['cli_anything.paste'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paste=cli_anything.paste:cli']},
)
