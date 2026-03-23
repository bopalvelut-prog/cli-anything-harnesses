from setuptools import setup
setup(
    name='cli-anything-cloudflare_tunnel',
    version='1.0.0',
    packages=['cli_anything.cloudflare_tunnel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_tunnel=cli_anything.cloudflare_tunnel:cli']},
)
