from setuptools import setup
setup(
    name='cli-anything-docutils',
    version='1.0.0',
    packages=['cli_anything.docutils'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-docutils=cli_anything.docutils:cli']},
)
