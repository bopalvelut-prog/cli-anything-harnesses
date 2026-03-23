import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('idea running')
@cli.command()
def start(): click.echo('idea started')
if __name__ == '__main__': cli()
