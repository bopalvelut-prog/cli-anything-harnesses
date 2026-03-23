import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vinyl running')
@cli.command()
def start(): click.echo('vinyl started')
if __name__ == '__main__': cli()
