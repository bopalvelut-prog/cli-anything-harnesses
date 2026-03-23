import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assembla running')
@cli.command()
def start(): click.echo('assembla started')
if __name__ == '__main__': cli()
