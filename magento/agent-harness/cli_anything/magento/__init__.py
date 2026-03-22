import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def setup(): subprocess.run(['bin/magento', 'setup:install'])
@cli.command()
def cache(): subprocess.run(['bin/magento', 'cache:flush'])
if __name__ == '__main__': cli()
