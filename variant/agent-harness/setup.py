from setuptools import setup
setup(
    name='cli-anything-variant',
    version='1.0.0',
    packages=['cli_anything.variant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-variant=cli_anything.variant:cli']},
)
