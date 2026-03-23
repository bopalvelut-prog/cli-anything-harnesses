import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('effect running')
@cli.command()
def start(): click.echo('effect started')
if __name__ == '__main__': cli()
