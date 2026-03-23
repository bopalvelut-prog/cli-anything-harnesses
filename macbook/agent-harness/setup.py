from setuptools import setup
setup(
    name='cli-anything-macbook',
    version='1.0.0',
    packages=['cli_anything.macbook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-macbook=cli_anything.macbook:cli']},
)
