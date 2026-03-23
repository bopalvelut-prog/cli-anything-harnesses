from setuptools import setup
setup(
    name='cli-anything-mention',
    version='1.0.0',
    packages=['cli_anything.mention'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mention=cli_anything.mention:cli']},
)
