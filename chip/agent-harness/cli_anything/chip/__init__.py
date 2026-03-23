import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chip running')
@cli.command()
def start(): click.echo('chip started')
if __name__ == '__main__': cli()
