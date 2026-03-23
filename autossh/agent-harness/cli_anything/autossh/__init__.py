import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autossh running')
@cli.command()
def start(): click.echo('autossh started')
if __name__ == '__main__': cli()
