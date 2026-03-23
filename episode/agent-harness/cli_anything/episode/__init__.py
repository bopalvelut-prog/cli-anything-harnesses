import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('episode running')
@cli.command()
def start(): click.echo('episode started')
if __name__ == '__main__': cli()
