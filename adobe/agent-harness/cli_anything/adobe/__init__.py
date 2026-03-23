import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adobe running')
@cli.command()
def start(): click.echo('adobe started')
if __name__ == '__main__': cli()
