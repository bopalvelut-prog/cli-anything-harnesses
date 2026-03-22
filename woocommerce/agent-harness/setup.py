from setuptools import setup
setup(
    name='cli-anything-woocommerce',
    version='1.0.0',
    packages=['cli_anything.woocommerce'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-woocommerce=cli_anything.woocommerce:cli']},
)
