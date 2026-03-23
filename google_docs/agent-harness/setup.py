from setuptools import setup
setup(
    name='cli-anything-google_docs',
    version='1.0.0',
    packages=['cli_anything.google_docs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_docs=cli_anything.google_docs:cli']},
)
