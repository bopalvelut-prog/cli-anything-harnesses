import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('longhorn running')
@cli.command()
def start(): click.echo('longhorn started')
if __name__ == '__main__': cli()
