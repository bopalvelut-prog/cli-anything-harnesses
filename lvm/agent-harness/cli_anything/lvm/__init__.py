import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['lvs'])
@cli.command()
def create(): click.echo('Creating LVM volume')
if __name__ == '__main__': cli()
