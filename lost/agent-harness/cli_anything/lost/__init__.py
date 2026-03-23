import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lost running')
@cli.command()
def start(): click.echo('lost started')
if __name__ == '__main__': cli()
