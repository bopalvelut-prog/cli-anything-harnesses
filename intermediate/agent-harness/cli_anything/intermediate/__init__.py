import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('intermediate running')
@cli.command()
def start(): click.echo('intermediate started')
if __name__ == '__main__': cli()
