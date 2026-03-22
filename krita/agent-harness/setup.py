from setuptools import setup
setup(
    name='cli-anything-krita',
    version='1.0.0',
    packages=['cli_anything.krita'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'cli-anything-krita=cli_anything.krita:cli',
        ],
    },
)
