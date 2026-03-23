import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('expense running')
@cli.command()
def start(): click.echo('expense started')
if __name__ == '__main__': cli()
