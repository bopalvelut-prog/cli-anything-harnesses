from setuptools import setup
setup(
    name='cli-anything-cloudflare_access',
    version='1.0.0',
    packages=['cli_anything.cloudflare_access'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_access=cli_anything.cloudflare_access:cli']},
)
