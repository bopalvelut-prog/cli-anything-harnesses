from setuptools import setup
setup(
    name='cli-anything-cloudflare_turnstile',
    version='1.0.0',
    packages=['cli_anything.cloudflare_turnstile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_turnstile=cli_anything.cloudflare_turnstile:cli']},
)
