from setuptools import setup
setup(
    name='cli-anything-shopify',
    version='1.0.0',
    packages=['cli_anything.shopify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shopify=cli_anything.shopify:cli']},
)
