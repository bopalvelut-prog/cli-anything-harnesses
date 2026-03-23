import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('netsuite running')
@cli.command()
def start(): click.echo('netsuite started')
if __name__ == '__main__': cli()
