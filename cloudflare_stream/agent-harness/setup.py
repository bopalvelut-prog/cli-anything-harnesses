from setuptools import setup
setup(
    name='cli-anything-cloudflare_stream',
    version='1.0.0',
    packages=['cli_anything.cloudflare_stream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_stream=cli_anything.cloudflare_stream:cli']},
)
