import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wolverine running')
@cli.command()
def start(): click.echo('wolverine started')
if __name__ == '__main__': cli()
