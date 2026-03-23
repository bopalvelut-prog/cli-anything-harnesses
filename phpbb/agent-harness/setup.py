from setuptools import setup
setup(
    name='cli-anything-phpbb',
    version='1.0.0',
    packages=['cli_anything.phpbb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phpbb=cli_anything.phpbb:cli']},
)
