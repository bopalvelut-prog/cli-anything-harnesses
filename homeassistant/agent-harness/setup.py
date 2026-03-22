from setuptools import setup
setup(
    name='cli-anything-homeassistant',
    version='1.0.0',
    packages=['cli_anything.homeassistant'],
    install_requires=['click', 'requests'],
    entry_points={
        'console_scripts': [
            'cli-anything-homeassistant=cli_anything.homeassistant:cli',
        ],
    },
)
