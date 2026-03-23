from setuptools import setup
setup(
    name='cli-anything-cloudflare_warp',
    version='1.0.0',
    packages=['cli_anything.cloudflare_warp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_warp=cli_anything.cloudflare_warp:cli']},
)
