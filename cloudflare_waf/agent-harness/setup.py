from setuptools import setup
setup(
    name='cli-anything-cloudflare_waf',
    version='1.0.0',
    packages=['cli_anything.cloudflare_waf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_waf=cli_anything.cloudflare_waf:cli']},
)
