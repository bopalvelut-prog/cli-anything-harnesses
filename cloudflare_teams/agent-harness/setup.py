from setuptools import setup
setup(
    name='cli-anything-cloudflare_teams',
    version='1.0.0',
    packages=['cli_anything.cloudflare_teams'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_teams=cli_anything.cloudflare_teams:cli']},
)
