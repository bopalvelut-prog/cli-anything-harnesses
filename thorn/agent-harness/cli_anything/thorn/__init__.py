import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thorn running')
@cli.command()
def start(): click.echo('thorn started')
if __name__ == '__main__': cli()
