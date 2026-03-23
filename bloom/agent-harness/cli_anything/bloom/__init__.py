import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bloom running')
@cli.command()
def start(): click.echo('bloom started')
if __name__ == '__main__': cli()
