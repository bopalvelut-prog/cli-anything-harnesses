import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('schema running')
@cli.command()
def start(): click.echo('schema started')
if __name__ == '__main__': cli()
