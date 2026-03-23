from setuptools import setup
setup(
    name='cli-anything-news',
    version='1.0.0',
    packages=['cli_anything.news'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-news=cli_anything.news:cli']},
)
