from setuptools import setup
setup(
    name='cli-anything-google_forms',
    version='1.0.0',
    packages=['cli_anything.google_forms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_forms=cli_anything.google_forms:cli']},
)
