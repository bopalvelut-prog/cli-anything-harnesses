import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('union running')
@cli.command()
def start(): click.echo('union started')
if __name__ == '__main__': cli()
