import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alien running')
@cli.command()
def start(): click.echo('alien started')
if __name__ == '__main__': cli()
