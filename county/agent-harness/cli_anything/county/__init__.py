import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('county running')
@cli.command()
def start(): click.echo('county started')
if __name__ == '__main__': cli()
