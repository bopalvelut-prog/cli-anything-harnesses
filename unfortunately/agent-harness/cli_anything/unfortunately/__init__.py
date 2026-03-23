import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unfortunately running')
@cli.command()
def start(): click.echo('unfortunately started')
if __name__ == '__main__': cli()
