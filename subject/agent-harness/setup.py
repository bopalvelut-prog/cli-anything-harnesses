from setuptools import setup
setup(
    name='cli-anything-subject',
    version='1.0.0',
    packages=['cli_anything.subject'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subject=cli_anything.subject:cli']},
)
