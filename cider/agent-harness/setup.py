from setuptools import setup
setup(
    name='cli-anything-cider',
    version='1.0.0',
    packages=['cli_anything.cider'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cider=cli_anything.cider:cli']},
)
