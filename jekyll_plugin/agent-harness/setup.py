from setuptools import setup
setup(
    name='cli-anything-jekyll_plugin',
    version='1.0.0',
    packages=['cli_anything.jekyll_plugin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jekyll_plugin=cli_anything.jekyll_plugin:cli']},
)
