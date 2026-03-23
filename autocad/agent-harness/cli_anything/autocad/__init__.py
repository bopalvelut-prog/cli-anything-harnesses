import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autocad running')
@cli.command()
def start(): click.echo('autocad started')
if __name__ == '__main__': cli()
