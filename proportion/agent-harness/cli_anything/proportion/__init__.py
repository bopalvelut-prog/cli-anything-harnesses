import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proportion running')
@cli.command()
def start(): click.echo('proportion started')
if __name__ == '__main__': cli()
