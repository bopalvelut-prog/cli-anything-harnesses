from setuptools import setup
setup(
    name='cli-anything-cloudflare_r2',
    version='1.0.0',
    packages=['cli_anything.cloudflare_r2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_r2=cli_anything.cloudflare_r2:cli']},
)
