from setuptools import setup
setup(
    name='cli-anything-amazon_securitylake',
    version='1.0.0',
    packages=['cli_anything.amazon_securitylake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_securitylake=cli_anything.amazon_securitylake:cli']},
)
