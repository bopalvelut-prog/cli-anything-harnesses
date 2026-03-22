from setuptools import setup
setup(
    name='cli-anything-obsidian',
    version='1.0.0',
    packages=['cli_anything.obsidian'],
    install_requires=['click', 'os'],
    entry_points={'console_scripts': ['cli-anything-obsidian=cli_anything.obsidian:cli']},
)
