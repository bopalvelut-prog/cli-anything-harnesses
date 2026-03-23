import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zigzag running')
@cli.command()
def start(): click.echo('zigzag started')
if __name__ == '__main__': cli()
