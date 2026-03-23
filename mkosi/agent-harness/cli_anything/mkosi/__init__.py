import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mkosi running')
@cli.command()
def start(): click.echo('mkosi started')
if __name__ == '__main__': cli()
