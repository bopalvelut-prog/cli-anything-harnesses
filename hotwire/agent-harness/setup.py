from setuptools import setup
setup(
    name='cli-anything-hotwire',
    version='1.0.0',
    packages=['cli_anything.hotwire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hotwire=cli_anything.hotwire:cli']},
)
