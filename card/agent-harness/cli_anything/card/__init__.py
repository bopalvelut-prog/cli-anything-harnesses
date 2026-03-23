import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('card running')
@cli.command()
def start(): click.echo('card started')
if __name__ == '__main__': cli()
