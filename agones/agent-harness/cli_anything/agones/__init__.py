import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('agones running')
@cli.command()
def start(): click.echo('agones started')
if __name__ == '__main__': cli()
