from setuptools import setup
setup(
    name='cli-anything-cloudflare_dns',
    version='1.0.0',
    packages=['cli_anything.cloudflare_dns'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_dns=cli_anything.cloudflare_dns:cli']},
)
