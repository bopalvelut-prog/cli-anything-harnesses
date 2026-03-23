import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kde running')
@cli.command()
def start(): click.echo('kde started')
if __name__ == '__main__': cli()
