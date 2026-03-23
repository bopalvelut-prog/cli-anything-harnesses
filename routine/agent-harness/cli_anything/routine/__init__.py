import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('routine running')
@cli.command()
def start(): click.echo('routine started')
if __name__ == '__main__': cli()
