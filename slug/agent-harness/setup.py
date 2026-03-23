from setuptools import setup
setup(
    name='cli-anything-slug',
    version='1.0.0',
    packages=['cli_anything.slug'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slug=cli_anything.slug:cli']},
)
