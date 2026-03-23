from setuptools import setup
setup(
    name='cli-anything-amazon_personalize',
    version='1.0.0',
    packages=['cli_anything.amazon_personalize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_personalize=cli_anything.amazon_personalize:cli']},
)
