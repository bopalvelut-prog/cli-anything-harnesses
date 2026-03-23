import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('treasure running')
@cli.command()
def start(): click.echo('treasure started')
if __name__ == '__main__': cli()
