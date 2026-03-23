import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('perfect running')
@cli.command()
def start(): click.echo('perfect started')
if __name__ == '__main__': cli()
