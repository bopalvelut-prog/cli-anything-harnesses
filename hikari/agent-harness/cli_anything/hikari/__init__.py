import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hikari running')
@cli.command()
def start(): click.echo('hikari started')
if __name__ == '__main__': cli()
