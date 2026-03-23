from setuptools import setup
setup(
    name='cli-anything-cloudflare_magic',
    version='1.0.0',
    packages=['cli_anything.cloudflare_magic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_magic=cli_anything.cloudflare_magic:cli']},
)
