import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jury running')
@cli.command()
def start(): click.echo('jury started')
if __name__ == '__main__': cli()
