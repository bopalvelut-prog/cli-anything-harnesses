import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grain running')
@cli.command()
def start(): click.echo('grain started')
if __name__ == '__main__': cli()
