from setuptools import setup
setup(
    name='cli-anything-newsblur',
    version='1.0.0',
    packages=['cli_anything.newsblur'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-newsblur=cli_anything.newsblur:cli']},
)
