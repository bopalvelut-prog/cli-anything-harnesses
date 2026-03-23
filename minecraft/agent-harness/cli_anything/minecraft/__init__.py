import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('minecraft running')
@cli.command()
def start(): click.echo('minecraft started')
if __name__ == '__main__': cli()
