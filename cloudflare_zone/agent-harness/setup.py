from setuptools import setup
setup(
    name='cli-anything-cloudflare_zone',
    version='1.0.0',
    packages=['cli_anything.cloudflare_zone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_zone=cli_anything.cloudflare_zone:cli']},
)
