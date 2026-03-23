from setuptools import setup
setup(
    name='cli-anything-cloudflare_zero',
    version='1.0.0',
    packages=['cli_anything.cloudflare_zero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_zero=cli_anything.cloudflare_zero:cli']},
)
