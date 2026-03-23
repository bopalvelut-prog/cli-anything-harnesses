import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('final running')
@cli.command()
def start(): click.echo('final started')
if __name__ == '__main__': cli()
