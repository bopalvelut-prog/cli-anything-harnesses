import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ginger running')
@cli.command()
def start(): click.echo('ginger started')
if __name__ == '__main__': cli()
