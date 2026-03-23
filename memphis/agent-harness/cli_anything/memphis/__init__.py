import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('memphis running')
@cli.command()
def start(): click.echo('memphis started')
if __name__ == '__main__': cli()
