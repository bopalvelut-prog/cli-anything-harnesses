import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('debmirror running')
@cli.command()
def start(): click.echo('debmirror started')
if __name__ == '__main__': cli()
