from setuptools import setup
setup(
    name='cli-anything-cloudflare_load',
    version='1.0.0',
    packages=['cli_anything.cloudflare_load'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_load=cli_anything.cloudflare_load:cli']},
)
