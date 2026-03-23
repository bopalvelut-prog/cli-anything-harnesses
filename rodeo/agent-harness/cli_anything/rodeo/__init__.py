import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rodeo running')
@cli.command()
def start(): click.echo('rodeo started')
if __name__ == '__main__': cli()
