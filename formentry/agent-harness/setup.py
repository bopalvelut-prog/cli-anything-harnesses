from setuptools import setup
setup(
    name='cli-anything-formentry',
    version='1.0.0',
    packages=['cli_anything.formentry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formentry=cli_anything.formentry:cli']},
)
