import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pair running')
@cli.command()
def start(): click.echo('pair started')
if __name__ == '__main__': cli()
