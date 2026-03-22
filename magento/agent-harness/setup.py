from setuptools import setup
setup(
    name='cli-anything-magento',
    version='1.0.0',
    packages=['cli_anything.magento'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-magento=cli_anything.magento:cli']},
)
