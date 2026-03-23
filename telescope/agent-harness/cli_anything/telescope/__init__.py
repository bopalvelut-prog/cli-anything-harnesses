import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('telescope running')
@cli.command()
def start(): click.echo('telescope started')
if __name__ == '__main__': cli()
