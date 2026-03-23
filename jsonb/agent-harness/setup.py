from setuptools import setup
setup(
    name='cli-anything-jsonb',
    version='1.0.0',
    packages=['cli_anything.jsonb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jsonb=cli_anything.jsonb:cli']},
)
