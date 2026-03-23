import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scheduler running')
@cli.command()
def start(): click.echo('scheduler started')
if __name__ == '__main__': cli()
