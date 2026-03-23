import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blank running')
@cli.command()
def start(): click.echo('blank started')
if __name__ == '__main__': cli()
