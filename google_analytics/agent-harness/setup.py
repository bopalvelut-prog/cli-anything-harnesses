from setuptools import setup
setup(
    name='cli-anything-google_analytics',
    version='1.0.0',
    packages=['cli_anything.google_analytics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_analytics=cli_anything.google_analytics:cli']},
)
