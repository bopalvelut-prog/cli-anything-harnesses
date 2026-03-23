from setuptools import setup
setup(
    name='cli-anything-article',
    version='1.0.0',
    packages=['cli_anything.article'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-article=cli_anything.article:cli']},
)
