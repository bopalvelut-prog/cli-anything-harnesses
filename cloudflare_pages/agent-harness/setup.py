from setuptools import setup
setup(
    name='cli-anything-cloudflare_pages',
    version='1.0.0',
    packages=['cli_anything.cloudflare_pages'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_pages=cli_anything.cloudflare_pages:cli']},
)
