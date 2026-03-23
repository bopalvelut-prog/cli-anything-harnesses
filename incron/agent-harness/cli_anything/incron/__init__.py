import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('incron running')
@cli.command()
def start(): click.echo('incron started')
if __name__ == '__main__': cli()
