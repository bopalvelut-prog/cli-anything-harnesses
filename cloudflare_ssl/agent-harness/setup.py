from setuptools import setup
setup(
    name='cli-anything-cloudflare_ssl',
    version='1.0.0',
    packages=['cli_anything.cloudflare_ssl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_ssl=cli_anything.cloudflare_ssl:cli']},
)
