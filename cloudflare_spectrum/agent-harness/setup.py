from setuptools import setup
setup(
    name='cli-anything-cloudflare_spectrum',
    version='1.0.0',
    packages=['cli_anything.cloudflare_spectrum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_spectrum=cli_anything.cloudflare_spectrum:cli']},
)
