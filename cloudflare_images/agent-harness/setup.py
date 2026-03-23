from setuptools import setup
setup(
    name='cli-anything-cloudflare_images',
    version='1.0.0',
    packages=['cli_anything.cloudflare_images'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudflare_images=cli_anything.cloudflare_images:cli']},
)
