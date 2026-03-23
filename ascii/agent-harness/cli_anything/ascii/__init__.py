import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ascii running')
@cli.command()
def start(): click.echo('ascii started')
if __name__ == '__main__': cli()
