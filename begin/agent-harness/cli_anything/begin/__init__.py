import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('begin running')
@cli.command()
def start(): click.echo('begin started')
if __name__ == '__main__': cli()
