import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('albion running')
@cli.command()
def start(): click.echo('albion started')
if __name__ == '__main__': cli()
