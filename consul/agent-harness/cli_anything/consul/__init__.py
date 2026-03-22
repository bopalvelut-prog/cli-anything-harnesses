import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def members(): subprocess.run(['consul', 'members'])
@cli.command()
def status(): subprocess.run(['consul', 'info'])
@cli.command()
def services(): subprocess.run(['consul', 'catalog', 'services'])
if __name__ == '__main__': cli()
