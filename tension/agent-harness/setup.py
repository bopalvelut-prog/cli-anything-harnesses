from setuptools import setup
setup(
    name='cli-anything-tension',
    version='1.0.0',
    packages=['cli_anything.tension'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tension=cli_anything.tension:cli']},
)
