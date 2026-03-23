import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('troll running')
@cli.command()
def start(): click.echo('troll started')
if __name__ == '__main__': cli()
