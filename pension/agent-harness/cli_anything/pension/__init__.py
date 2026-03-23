import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pension running')
@cli.command()
def start(): click.echo('pension started')
if __name__ == '__main__': cli()
