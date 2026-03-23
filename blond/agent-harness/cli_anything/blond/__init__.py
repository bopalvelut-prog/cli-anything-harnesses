import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blond running')
@cli.command()
def start(): click.echo('blond started')
if __name__ == '__main__': cli()
