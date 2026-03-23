from setuptools import setup
setup(
    name='cli-anything-plymouth',
    version='1.0.0',
    packages=['cli_anything.plymouth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plymouth=cli_anything.plymouth:cli']},
)
