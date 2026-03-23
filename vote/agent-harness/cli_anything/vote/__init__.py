import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vote running')
@cli.command()
def start(): click.echo('vote started')
if __name__ == '__main__': cli()
