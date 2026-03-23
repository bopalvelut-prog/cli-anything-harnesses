from setuptools import setup
setup(
    name='cli-anything-category',
    version='1.0.0',
    packages=['cli_anything.category'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-category=cli_anything.category:cli']},
)
