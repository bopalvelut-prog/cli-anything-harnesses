from setuptools import setup
setup(
    name='cli-anything-obsidian_vault',
    version='1.0.0',
    packages=['cli_anything.obsidian_vault'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-obsidian_vault=cli_anything.obsidian_vault:cli']},
)
