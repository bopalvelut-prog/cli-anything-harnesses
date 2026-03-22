from setuptools import setup
setup(
    name='cli-anything-deno',
    version='1.0.0',
    packages=['cli_anything.deno'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deno=cli_anything.deno:cli']},
)
