import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('decide running')
@cli.command()
def start(): click.echo('decide started')
if __name__ == '__main__': cli()
