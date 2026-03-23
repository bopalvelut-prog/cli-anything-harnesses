import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('timber running')
@cli.command()
def start(): click.echo('timber started')
if __name__ == '__main__': cli()
