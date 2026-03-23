from setuptools import setup
setup(
    name='cli-anything-discordpy',
    version='1.0.0',
    packages=['cli_anything.discordpy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-discordpy=cli_anything.discordpy:cli']},
)
