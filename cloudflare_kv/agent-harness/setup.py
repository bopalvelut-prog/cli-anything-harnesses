from setuptools import setup
setup(
    name='cli-anything-cloudflare_kv',
    version='1.0.0',
    packages=['cli_anything.cloudflare_kv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_kv=cli_anything.cloudflare_kv:cli']},
)
