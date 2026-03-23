from setuptools import setup
setup(
    name='cli-anything-during',
    version='1.0.0',
    packages=['cli_anything.during'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-during=cli_anything.during:cli']},
)
