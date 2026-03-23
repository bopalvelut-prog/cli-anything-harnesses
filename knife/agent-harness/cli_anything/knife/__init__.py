import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('knife running')
@cli.command()
def start(): click.echo('knife started')
if __name__ == '__main__': cli()
