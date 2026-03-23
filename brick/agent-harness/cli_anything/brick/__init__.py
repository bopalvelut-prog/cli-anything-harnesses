import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('brick running')
@cli.command()
def start(): click.echo('brick started')
if __name__ == '__main__': cli()
