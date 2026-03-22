from setuptools import setup
setup(
    name='cli-anything-firefox',
    version='1.0.0',
    packages=['cli_anything.firefox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firefox=cli_anything.firefox:cli']},
)
