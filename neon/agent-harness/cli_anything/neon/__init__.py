import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('neon running')
@cli.command()
def start(): click.echo('neon started')
if __name__ == '__main__': cli()
