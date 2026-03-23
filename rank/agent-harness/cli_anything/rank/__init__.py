import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rank running')
@cli.command()
def start(): click.echo('rank started')
if __name__ == '__main__': cli()
