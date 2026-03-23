import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spiffe running')
@cli.command()
def start(): click.echo('spiffe started')
if __name__ == '__main__': cli()
