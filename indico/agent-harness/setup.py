from setuptools import setup
setup(
    name='cli-anything-indico',
    version='1.0.0',
    packages=['cli_anything.indico'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-indico=cli_anything.indico:cli']},
)
