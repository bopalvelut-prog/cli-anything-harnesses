import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stone running')
@cli.command()
def start(): click.echo('stone started')
if __name__ == '__main__': cli()
