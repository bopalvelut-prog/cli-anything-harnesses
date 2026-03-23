from setuptools import setup
setup(
    name='cli-anything-bear',
    version='1.0.0',
    packages=['cli_anything.bear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bear=cli_anything.bear:cli']},
)
