from setuptools import setup
setup(
    name='cli-anything-wagtail',
    version='1.0.0',
    packages=['cli_anything.wagtail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wagtail=cli_anything.wagtail:cli']},
)
