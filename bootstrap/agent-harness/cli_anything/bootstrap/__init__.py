import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bootstrap running')
@cli.command()
def start(): click.echo('bootstrap started')
if __name__ == '__main__': cli()
