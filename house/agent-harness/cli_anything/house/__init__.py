import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('house running')
@cli.command()
def start(): click.echo('house started')
if __name__ == '__main__': cli()
